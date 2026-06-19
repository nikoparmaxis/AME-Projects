import numpy as np
from scipy.interpolate import interp1d
from scipy.integrate import solve_ivp

def road_profile(x, profile_type):
    yr = np.zeros_like(x)
    if profile_type == 1:
        xc = 5.0
        h = 0.1
        w = 0.5
        yr = h * np.exp(-((x - xc)**2) / (w**2))
    elif profile_type == 2:
        xc = 5.0
        h = -0.08
        w = 0.3
        t_trans = 0.02
        term1 = 1 + np.tanh((x - (xc - w/2)) / t_trans)
        term2 = 1 - np.tanh((x - (xc + w/2)) / t_trans)
        yr = (h / 4) * term1 * term2
    elif profile_type == 3:
        h = 0.02
        lambda_x = 15.0
        yr = h * np.sin(2 * np.pi * x / lambda_x)
    elif profile_type == 4:
        np.random.seed(42)
        n = int(np.max(x) / 3.0)
        h_max = 0.03
        w = 2.0
        xi = np.random.uniform(0, np.max(x), n)
        hi = np.random.uniform(-h_max, h_max, n)
        yr = np.zeros_like(x)
        for i in range(n):
            yr += hi[i] * np.exp(-((x - xi[i]) / w)**2)       
    else:
        raise ValueError("Profile type must be 1, 2, 3, or 4")
    return yr
def suspension_ode(t, y, m_c, m_w, k_2, c, k_1, y_r_interp):
    y1 = y[0] 
    y2 = y[1] 
    y3 = y[2] 
    y4 = y[3]
    yr = y_r_interp(t)
    dy1dt = y2
    dy2dt = -(k_2 / m_c) * (y1 - y3) - (c / m_c) * (y2 - y4)
    dy3dt = y4
    dy4dt = (k_2 / m_w) * (y1 - y3) + (c / m_w) * (y2 - y4) - (k_1 / m_w) * (y3 - yr)
    return np.array([dy1dt, dy2dt, dy3dt, dy4dt])
def simulate_suspension(m_c, m_w, k_2, c, k_1, x, y_r, v_c):
    t_road = x / v_c
    y_r_interp = interp1d(t_road, y_r, kind='linear', fill_value="extrapolate")
    t_end = t_road[-1]
    t_span = (0, t_end)
    t_eval = np.linspace(0, t_end, 2000)
    y0 = np.array([0.0, 0.0, 0.0, 0.0])
    sol = solve_ivp(
        suspension_ode,
        t_span,
        y0,
        t_eval=t_eval,
        max_step=0.001,
        args=(m_c, m_w, k_2, c, k_1, y_r_interp))
    t = sol.t
    y_full = sol.y
    y_c = y_full[0, :]
    yp_c = y_full[1, :]
    y_w = y_full[2, :]
    yp_w = y_full[3, :]
    ypp_c = -(k_2 / m_c) * (y_c - y_w) - (c / m_c) * (yp_c - yp_w)
    return t, y_c, yp_c, ypp_c
def calculate_performance_metrics(t, y_c, yp_c, ypp_c):
    rms_val = np.sqrt(np.mean(ypp_c**2))
    max_displacement = np.max(np.abs(y_c))
    return rms_val, max_displacement