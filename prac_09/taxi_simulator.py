from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def display_taxis(taxis):
    """Print the list of available taxis with their index."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")