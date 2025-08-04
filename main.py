from ppadb.client import Client as AdbClient


client = AdbClient(host="127.0.0.1", port=5037)  # Default is "127.0.0.1" and 5037
devices = client.devices()[0]

battery_log = devices.shell("dumpsys battery")
print(battery_log)
