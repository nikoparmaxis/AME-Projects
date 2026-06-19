
import numpy as np
from scipy.interpolate import interp1d
from scipy.integrate import cumulative_trapezoid, trapezoid

def calculate_inertia(x, design, l_bridge, b_bridge):
    h = np.zeros_like(x)
    if design == 1:
        h[:] = 5.0
    elif design == 2:
        term = (2 * np.abs(x - l_bridge/2)) / l_bridge
        h = 2.5 + 2.5 * (1 - term)
    elif design == 3:
        term = ((2 * x - l_bridge) / l_bridge)**2
        h = 2.5 + 2.5 * (1 - term)
    elif design == 4:
        term = ((2 * x - l_bridge) / l_bridge)**2
        h = 2.5 + 2.5 * term
    else:
        raise ValueError("Design must be 1, 2, 3, or 4")
    I = (b_bridge * h**3) / 12.0
    return I

def interpolate_load(x_data, f_data, x):
    interpolator = interp1d(x_data, f_data, kind='linear', axis=0, fill_value="extrapolate")
    f_interp = interpolator(x)
    return f_interp

def calculate_deflection(x, f, i_bridge, e_modulus, l_bridge):
    integrand_ra = (l_bridge - x) * f
    r_a = trapezoid(integrand_ra, x) / l_bridge
    shear_integral = cumulative_trapezoid(f, x, initial=0)
    v = r_a - shear_integral
    int_f = cumulative_trapezoid(f, x, initial=0)
    int_xf = cumulative_trapezoid(x * f, x, initial=0)
    m_moment = r_a * x - (x * int_f - int_xf)
    kappa = m_moment / (e_modulus * i_bridge)
    theta_0 = cumulative_trapezoid(kappa, x, initial=0)
    y_0 = cumulative_trapezoid(theta_0, x, initial=0)
    y_0_0 = y_0[0]
    y_0_L = y_0[-1]
    y = y_0 - y_0_0 - (x / l_bridge) * (y_0_L - y_0_0)
    
    return y

def analyze_design(x, f_interp, design, e_modulus, l_bridge, b_bridge):
    i_bridge = calculate_inertia(x, design, l_bridge, b_bridge)
    n_times = f_interp.shape[1]
    y = np.zeros((len(x), n_times))
    for t in range(n_times):
        f_t = f_interp[:, t]
        y[:, t] = calculate_deflection(x, f_t, i_bridge, e_modulus, l_bridge)
    
    print(f"y shape: {y.shape}")
    print(f"y min/max per column (time step):")
    for t in range(n_times):
        print(f"  Time {t}: min={np.min(y[:, t]):.6f}, max={np.max(y[:, t]):.6f}, abs_max={np.max(np.abs(y[:, t])):.6f}")
    
    y_max = np.max(np.abs(y), axis=0)
    deflection_metric = trapezoid(y_max, dx=1.0)
    
    print(f"\ny_max shape: {y_max.shape}")  
    print(f"y_max values: {y_max}")
    print(f"deflection_metric: {deflection_metric}")
    
    return y, y_max, deflection_metric