from devices.device import Device
from devices.sysvar import SysVar

DEVICES = [
    Device(
        name="Licht Gartenseite:Aktor:2 - STATE",
        address="000B9A498D76F0",
        channel=2,
        parameter="STATE"
    ),
    Device(
        name="Licht Strassenseite:Aktor:2 - STATE",
        address="000B9A498D747D",
        channel=2,
        parameter="STATE"
    ),
    SysVar(
        name="MQTT.Test",
        address="9292"
    )
]
