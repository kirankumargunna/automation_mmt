class homepagedata:
    list_your_properties_pageTitle="Goibibo & MakeMytrip - Free Hotel Registration - Add your Hotel with Connect (Ingo-MMT)"

    elements_navigation_bar=["Flights", "Hotels", "Homestays & Villas", "Holiday Packages", "Trains", "Buses", "Cabs", "Forex Card & Currency", "Travel Insurance"]

    # List of cities for MMT
    Domestic_cities = ["Delhi", "Mumbai", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Lucknow"]

    International_cities=["Dubai", "Singapore", "London", "New York", "Paris","Bangkok", "Sydney", "Toronto", "Kuala Lumpur", "Tokyo" ]

    travel_date= "Feb 28, 2025"



class flightpageData:
    
    Trip_types=['One Way', 'Round Trip', 'Multi City']  

    Fare_types=['Regular', 'student', 'senior Citizen', 'Armed Forces', 'Doctor and Nurse']

    Filters=['Applied Filters', 
             'Popular Filters', 
             'One Way Price', 
             f'Stops From {homepagedata.Domestic_cities[1]}',
             f'Depature From {homepagedata.Domestic_cities[1]}',
             f'Arrival at {homepagedata.International_cities[1]}',
             'Airlines'
               ]
    
