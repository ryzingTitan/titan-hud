import obd

connection = obd.OBD("/dev/ttyUSB0")

# python-OBD automatically queries supported PIDs on connect
# and filters out unsupported ones
print("Supported commands:")
for cmd in connection.supported_commands:
    print(f"  {cmd.name} (PID {hex(cmd.pid)}): {cmd.desc}")