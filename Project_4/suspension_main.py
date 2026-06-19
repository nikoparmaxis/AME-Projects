import numpy as np
import suspension_utils as su

def main():
    m_c = 400.0       
    m_w = 40.0       
    k_1 = 180000.0    
    configs = {
        "Comfort":  {"k2": 12000.0, "c": 2200.0},
        "Sport":    {"k2": 35000.0, "c": 1500.0},
        "Off-road": {"k2": 25000.0, "c": 1600.0},
        "Race":     {"k2": 50000.0, "c": 1000.0}
    }
    v_c_mph = 50.0
    v_c = v_c_mph * 0.44704
    x_max = 100.0
    n_points = 5000
    x = np.linspace(0, x_max, n_points)
    road_types = {
        1: "Speed Bump",
        2: "Pothole",
        3: "Sinusoidal Pattern",
        4: "Rough Road"
    }
    config_names = ["Comfort", "Sport", "Off-road", "Race"]
    for type_id in range(1, 5):
        road_name = road_types[type_id]
        print(f"Road Profile: {road_name}")
        y_r = su.road_profile(x, type_id)
        for config_name in config_names:
            params = configs[config_name]
            k_2 = params["k2"]
            c_val = params["c"]
            t, y_c, yp_c, ypp_c = su.simulate_suspension(m_c, m_w, k_2, c_val, k_1, x, y_r, v_c)
            rms, max_disp = su.calculate_performance_metrics(t, y_c, yp_c, ypp_c)
            print(f"{config_name:<10s}: rms_val = {rms:.4f} m/s^2, max_displacement = {max_disp*1000:.2f} mm")
        print("-" * 65) 
if __name__ == "__main__":
    main()