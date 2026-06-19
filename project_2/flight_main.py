import trajectory_utils as tu

def main():
    airspeed = 200
    min_distance = float('inf')
    min_time = float('inf')
    min_fuel = float('inf') 

    min_distance_day = ""
    min_time_day = ""           
    min_fuel_day = ""   

    monday_legs = [
        (0,0,100,0,45,2),
        (100,0,175,100,90,5),
        (175,100,250,50,135,25),
        (250,50,300,100,225,30)
    ]

    dist, time, fuel = tu.route_analysis(monday_legs, airspeed)
    print(f"\nMonday route:")        
    print(f"Total distance:{dist:.2f} km")
    print(f"Total flight time:{time:.2f} h")
    print(f"Total fuel needed:{fuel:.2f} l/h")

    if dist < min_distance:
            min_distance = dist
            min_distance_day = "Monday"
    if time < min_time:
            min_time = time
            min_time_day = "Monday"
    if fuel < min_fuel:
            min_fuel = fuel
            min_fuel_day = "Monday"

    tuesday_legs = [
        (0,0,150,0,135,5),
        (150,0,225,-40,270,15),
        (225,-40,300,100,45,28)
    ]
    dist, time, fuel = tu.route_analysis(tuesday_legs, airspeed)
    print(f"\nTuesday route:")
    print(f"Total distance:{dist:.2f} km")          
    print(f"Total flight time:{time:.2f} h")
    print(f"Total fuel needed:{fuel:.2f} l/h")

    if dist < min_distance:
            min_distance = dist
            min_distance_day = "Tuesday"    
    if time < min_time:
            min_time = time
            min_time_day = "Tuesday"
    if fuel < min_fuel:
            min_fuel = fuel
            min_fuel_day = "Tuesday"

    wednesday_legs = [
        (0,0,250,-50,180,25),
        (250,-50,300,100,225,40)
    ]
    dist, time, fuel = tu.route_analysis(wednesday_legs, airspeed)
    print(f"\nWednesday route:")
    print(f"Total distance:{dist:.2f} km")          
    print(f"Total flight time:{time:.2f} h")
    print(f"Total fuel needed:{fuel:.2f} l/h")

    if dist < min_distance:
            min_distance = dist
            min_distance_day = "Wednesday"
    if time < min_time:
            min_time = time
            min_time_day = "Wednesday"
    if fuel < min_fuel:
            min_fuel = fuel
            min_fuel_day = "Wednesday"

    thursday_legs = [
        (0,0,0,100,0,5),
        (0,100,200,100,45,5),
        (200,100,250,50,315,33),
        (250,50,300,100,45,10)
    ]
    dist, time, fuel = tu.route_analysis(thursday_legs, airspeed)
    print(f"\nThursday route:")
    print(f"Total distance:{dist:.2f} km")  
    print(f"Total flight time:{time:.2f} h")
    print(f"Total fuel needed:{fuel:.2f} l/h")

    if dist < min_distance:
            min_distance = dist
            min_distance_day = "Thursday"
    if time < min_time:
            min_time = time
            min_time_day = "Thursday"
    if fuel < min_fuel:
            min_fuel = fuel
            min_fuel_day = "Thursday"

    print("\nRecommendations")
    print(f"Shortest distance: {min_distance:.2f} km ({min_distance_day})")
    print(f"Shortest flight time: {min_time:.2f} h ({min_time_day})")
    print(f"Lowest fuel consumption: {min_fuel:.2f} liters ({min_fuel_day})")

if __name__ == "__main__":
    main()