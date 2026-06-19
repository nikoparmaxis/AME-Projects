import launch_checks as lc
# Case A 

temp_C = 20 
wind_ms = 10
fuel_percent = 95
battery_V = 25 

ok_weather = lc.weather_ok (temp_C,wind_ms)
ok_system = lc.systems_ok (fuel_percent,battery_V)

if ok_weather and (ok_system):
    print("launch approved")

elif (not ok_weather) and (not ok_system):
    print("launch hold")
    print("warning: weather outside limits.")
    print("warning: systems not ready.")

elif not ok_weather:
    print("launch hold")
    print("warning: weather outside limits.")

else:
    print("launch hold")
    print("warning: systems not ready.")


# case B

temp_C = -15 
wind_ms = 5
fuel_percent = 92
battery_V = 24.5

ok_weather = lc.weather_ok (temp_C,wind_ms)
ok_system = lc.systems_ok (fuel_percent,battery_V)

if ok_weather and (ok_system):
    print("launch approved")

elif (not ok_weather) and (not ok_system):
    print("launch hold")
    print("warning: weather outside limits.")
    print("warning: systems not ready.")

elif not ok_weather:
    print("launch hold")
    print("warning: weather outside limits.")

else:
    print("launch hold")
    print("warning: systems not ready.")

    
# case C 

temp_C = 25 
wind_ms = 14.9
fuel_percent = 85
battery_V = 23.8 

ok_weather = lc.weather_ok (temp_C,wind_ms)
ok_system = lc.systems_ok (fuel_percent,battery_V)

if ok_weather and (ok_system):
    print("launch approved")

elif (not ok_weather) and (not ok_system):
    print("launch hold")
    print("warning: weather outside limits.")
    print("warning: systems not ready.")

elif not ok_weather:
    print("launch hold")
    print("warning: weather outside limits.")

else:
    print("launch hold")
    print("warning: systems not ready.")


# case D

temp_C = 36 
wind_ms = 16
fuel_percent = 80
battery_V = 23 

ok_weather = lc.weather_ok (temp_C,wind_ms)
ok_system = lc.systems_ok (fuel_percent,battery_V)

if ok_weather and (ok_system):
    print("launch approved")

elif (not ok_weather) and (not ok_system):
    print("launch hold")
    print("warning: weather outside limits.")
    print("warning: systems not ready.")

elif not ok_weather:
    print("launch hold")
    print("warning: weather outside limits.")

else:
    print("launch hold")
    print("warning: systems not ready.")

