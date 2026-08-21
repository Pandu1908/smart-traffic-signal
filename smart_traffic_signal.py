print("🚦 SMART TRAFFIC SIGNAL")

vehicle_count = int(input("Enter number of vehicles: "))

if vehicle_count > 50:
    print("🔴 Heavy traffic - RED signal")
elif vehicle_count > 20:
    print("🟡 Moderate traffic - YELLOW signal")
else:
    print("🟢 Low traffic - GREEN signal")
