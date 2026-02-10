import time
import random

altitude = 0.0        # meters
battery = 100.0       # percent
latitude = 17.3850    # sample GPS (India)
longitude = 78.4867

print("Starting Drone Telemetry Simulation...\n")

for second in range(1, 31):
    altitude += random.uniform(0.5, 2.0)
    speed = random.uniform(10, 25)
    battery -= random.uniform(0.5, 1.0)

    latitude += random.uniform(-0.0001, 0.0001)
    longitude += random.uniform(-0.0001, 0.0001)

    print(f"Time: {second} sec")
    print(f"Altitude : {altitude:.2f} m")
    print(f"Speed    : {speed:.2f} m/s")
    print(f"Battery  : {battery:.2f} %")
    print(f"GPS      : ({latitude:.6f}, {longitude:.6f})")
    print("-" * 30)

    time.sleep(1)

print("\nTelemetry Simulation Completed.")
