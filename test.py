class FlightPageData:
    def __init__(self):
        self.filters = [
            f'Stops From {HomePageData.domestic_cities[1]}',  # Evaluated when an instance is created
        ]
        print("FlightPageData instance created.")


class HomePageData:
    # Some static data for the homepage
    domestic_cities = ["Delhi", "Mumbai", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Lucknow"]
    international_cities = ["Dubai", "Singapore", "London", "New York", "Paris", "Bangkok", "Sydney", "Toronto", "Kuala Lumpur", "Tokyo"]
    print("HomePageData class initialized.")



# Trigger class definition and instantiation
FlightPageData # This will try to access HomePageData class-level variables
