from unreliable_car import UnreliableCar

def main():
    reliable_car = UnreliableCar("Reliable", 100, 100)
    unreliable_car = UnreliableCar("Unreliable", 100, 30)

    print("Testing 100% reliable car:")
    for i in range(5):
        distance = reliable_car.drive(10)
        print(f"Attempt {i + 1}: Drove {distance} km")

    print("\nTesting 30% unreliable car (100 attempts):")
    drive_count = 0
    total_attempts = 100
    for i in range(total_attempts):
        distance = unreliable_car.drive(1)
        if distance > 0:
            drive_count += 1

    print(f"Drove successfully {drive_count} times out of {total_attempts} attempts")
    print(f"Estimated reliability: {drive_count}%")

main()