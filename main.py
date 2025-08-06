import os
import subprocess
import re
from ppadb.client import Client as AdbClient


battery_info = {
    "mSavedBatteryAsoc": None,
    "mSavedBatteryUsage": None,
    "Charge counter": None,
    "level": None,
}
device_typical_capacity = 4900


def calc_battery_info(battery_info, device_typical_capacity):
    """배터리 정보 계산
    adb로 추출한 battery_log를 바탕으로 배터리 정보를 계산

    Args:
        battery_info (dict): 배터리 정보
        device_typical_capacity (int): 배터리 용량

    Returns:
        battery_life (int): 배터리 수명(단위: %)
        battery_life_calculated (int): 계산한 배터리 수명(단위: %)
        battery_cycle_count (int): 배터리 사이클(단위: 회)
    """
    charge_counter_str = battery_info["Charge counter"]
    charge_counter_float = float(f"{charge_counter_str[:4]}.{charge_counter_str[4:]}")

    battery_life = battery_info["mSavedBatteryAsoc"]
    battery_life_calculated = round(
        charge_counter_float
        / (int(battery_info["level"]) / 100)
        / device_typical_capacity
        * 100,
        2,
    )
    battery_cycle_count = round(int(battery_info["mSavedBatteryUsage"]) / 100)

    return battery_life, battery_life_calculated, battery_cycle_count


# start adb server
script_dir = os.path.dirname(os.path.abspath(__file__))
platform_tools_path = os.path.join(script_dir, "platform-tools")
os.chdir(platform_tools_path)
subprocess.run(["adb", "start-server"], check=True)

client = AdbClient(host="127.0.0.1", port=5037)  # Default is "127.0.0.1" and 5037
devices = client.devices()[0]

battery_log = devices.shell("dumpsys battery")

for line in battery_log.splitlines():
    match = re.match(r"^\s*([^:]+):\s*(.*)$", line)

    if match:
        key = match.group(1).strip()
        if key in battery_info and battery_info[key] == None:
            value = match.group(2).strip(" []")
            battery_info[key] = value


battery_life, battery_life_calculated, battery_cycle_count = calc_battery_info(
    battery_info, device_typical_capacity
)

print("===== battery info =====")
print(f"Battery Life: {battery_life}%")
print(f"Battery Life(Calculated): {battery_life_calculated}%")
print(f"Battery Cycle Count: {battery_cycle_count}")


client.remote_disconnect()
subprocess.run(["adb", "kill-server"])
