import re
from ppadb.client import Client as AdbClient


client = AdbClient(host="127.0.0.1", port=5037)  # Default is "127.0.0.1" and 5037
devices = client.devices()[0]

battery_log = devices.shell("dumpsys battery")
print(battery_log)

battery_info = {
    "mSavedBatteryAsoc": "None",
    "mSavedBatteryUsage": "None",
    "Charge counter": "None",
    "level": "None",
}

for line in battery_log.splitlines():

    match = re.match(r"^\s*([^:]+):\s*(.*)$", line)
    if match:
        key = match.group(1).strip()

        if key in battery_info and battery_info[key] == "None":
            value = match.group(2).strip(" []")
            battery_info[key] = value

print(f"battery_info = {battery_info}")

client.remote_disconnect()
