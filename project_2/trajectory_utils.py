#function 1 
import math
def leg_analysis (x1,y1,x2,y2,wind_angle_deg,wind_speed_mag,airspeed):
    d_x = x2 - x1
    d_y = y2 - y1
    d = math.sqrt(d_x**2 + d_y**2)

    flight_path_angle_rad = math.atan2(d_y, d_x)
    theta_flight_deg = math.degrees(flight_path_angle_rad)
    theta_flight_deg = theta_flight_deg % 360

    relative_wind_angle_degree = (wind_angle_deg - theta_flight_deg) 
    relative_wind_angle_rad = math.radians(relative_wind_angle_degree)
    relative_wind_angle = (math.cos(relative_wind_angle_rad))

    delta_v = wind_speed_mag * relative_wind_angle 
   
    ground_speed = airspeed + delta_v
    flight_time = d / ground_speed   

    return d, flight_time

#function 2
def classify_wind_conditions (wind_speed_mag):
    if 0<= wind_speed_mag <=5:
        wind_condition="quiet"
    elif 6<= wind_speed_mag <=15:
            wind_condition="windy"
    elif 16<= wind_speed_mag <=25:
            wind_condition="gusty"
    elif 26<= wind_speed_mag <=40:
            wind_condition="stormy"
    else:
            wind_condition="stormy"
    return wind_condition

#function 3
def fuel_consumption (flight_time,wind_condition):
    f_b = 45  # liters per hour
    t = flight_time
    if wind_condition == "quiet":
        p = 0.0
    elif wind_condition == "windy":
        p = 0.05
    elif wind_condition == "gusty":
        p = 0.10
    elif wind_condition == "stormy":
        p = 0.15
    else:
        p = 0.0 
    f_c = f_b * (1 + p) * t
    return f_c

#function 4
def route_analysis (legs,airspeed):
    distance_total = 0.0
    time_total = 0.0
    fuel_total = 0.0

    for leg in legs:
          x1,y1,x2,y2,wind_angle_deg,wind_speed_mag = leg
          dist, time = leg_analysis(x1, y1, x2, y2, wind_angle_deg, wind_speed_mag, airspeed)
          condition = classify_wind_conditions(wind_speed_mag)
          fuel = fuel_consumption (time,condition)

          distance_total += dist
          time_total += time
          fuel_total += fuel
    return distance_total, time_total, fuel_total