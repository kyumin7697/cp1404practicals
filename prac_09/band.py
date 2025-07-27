class Band:
    """A Band has a name and a list of Musicians."""

    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return string kinds of BandName (musician1, musician2, ...)"""
        musician_strs = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_strs})"

    def play(self):
        """Make each musician play their first instrument."""
        for musician in self.musicians:
            if musician.instruments:
                print(f"{musician.name} is playing: {musician.instruments[0]}")
            else:
                print(f"{musician.name} needs an instrument!")