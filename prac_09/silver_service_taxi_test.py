from silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Hummer", 200, 2)  # fanciness=2 → price_per_km = 1.23 * 2 = 2.46
    taxi.start_fare()
    taxi.drive(18)

    print(taxi)
    fare = taxi.get_fare()
    print(f"Fare for 18 km: ${fare:.2f}")

    expected_fare = (18 * 2.46) + 4.50  # = 48.78
    assert abs(fare - expected_fare) < 0.01, f"Expected ${expected_fare:.2f}, got ${fare:.2f}"

main()