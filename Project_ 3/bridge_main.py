import numpy as np
import os
import bridge_utils

def main():
    # --- 1. Define Parameters ---
    l_bridge = 100.0      # Length in m
    e_modulus = 35.0e9    # Young's Modulus in Pa
    b_bridge = 10.0       # Width in m
    n_points = 201        # Grid points
    
    # --- 2. Discretize x ---
    x = np.linspace(0, l_bridge, n_points)
    
    # --- 3. Load Traffic Data ---
    filename = 'traffic_loads.npy'
    
    # Check if file exists (Safety check for local running)
    if not os.path.exists(filename):
        print(f"Error: {filename} not found. Please ensure it is in the same directory.")
        # Optional: You could generate dummy data here for testing if needed, 
        # but for submission you must rely on the file existing.
        return

    data = np.load(filename)
    
    # Parse data: Col 0 is x_data, Cols 1-24 are f(x,t)
    x_data = data[:, 0]
    f_data = data[:, 1:]
    
    # --- 4. Interpolate Load ---
    f_interp = bridge_utils.interpolate_load(x_data, f_data, x)
    
    # --- 5. Analyze Designs ---
    results = []
    print("\nBridge Analysis:")
    
    for design_id in range(1, 5):
        _, _, metric = bridge_utils.analyze_design(
            x, f_interp, design_id, e_modulus, l_bridge, b_bridge)
        
        results.append(metric)
        print(f"Design {design_id}: deflection_metric = {metric:.4f} m*h")
    
    # --- 6. Determine Optimal Design ---
    optimal_idx = np.argmin(results)
    optimal_design = optimal_idx + 1
    
    print(f"\nOptimal design: Design {optimal_design} (minimum deflection metric)")

if __name__ == "__main__":
    main()