import os
import subprocess
import re
from ppadb.client import Client as AdbClient


device_typical_capacity = 4900
battery_info = {
    "mSavedBatteryAsoc": "None",
    "mSavedBatteryUsage": "None",
    "Charge counter": "None",
    "level": "None",
}


# start adb server
script_dir = os.path.dirname(os.path.abspath(__file__))
platform_tools_path = os.path.join(script_dir, "platform-tools")
os.chdir(platform_tools_path)
subprocess.run(["adb", "start-server"], check=True)


client = AdbClient(host="127.0.0.1", port=5037)  # Default is "127.0.0.1" and 5037
devices = client.devices()[0]

battery_log = devices.shell("dumpsys battery")
print(battery_log)


for line in battery_log.splitlines():
    match = re.match(r"^\s*([^:]+):\s*(.*)$", line)

    if match:
        key = match.group(1).strip()

        if key in battery_info and battery_info[key] == "None":
            value = match.group(2).strip(" []")
            battery_info[key] = value

charge_counter_str = battery_info["Charge counter"]
charge_counter_float = float(f"{charge_counter_str[:4]}.{charge_counter_str[4:]}")


print("===== battery info =====")
print(f"Battery Life: {battery_info['mSavedBatteryAsoc']}%")
print(
    f"Battery Life(Calculated): {round(charge_counter_float / (int(battery_info['level'])/100) / device_typical_capacity * 100, 2)}%"
)
print(f"Battery Cycle Count: {round(int(battery_info['mSavedBatteryUsage']) / 100)}")


client.remote_disconnect()
subprocess.run(["adb", "kill-server"])
