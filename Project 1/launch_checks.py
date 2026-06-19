def weather_ok(temp_C,wind_ms):
    return (-10<=temp_C and temp_C<=35 and wind_ms<15)
def systems_ok(fuel_percent,battery_V):
    return (fuel_percent>=90 and battery_V>=24)
    