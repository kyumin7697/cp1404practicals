from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised Taxi with higher fares based on fanciness and flagfall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return fare including flagfall."""
        return super().get_fare() + SilverServiceTaxi.flagfall

    def __str__(self):
        """Return a string like Taxi, but with flagfall included."""
        return f"{super().__str__()} plus flagfall of ${SilverServiceTaxi.flagfall:.2f}"