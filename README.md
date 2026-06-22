# AME-Projects

Engineering analysis and simulation scripts built for coursework, applying numerical methods (NumPy, SciPy) to structural, aerospace, and vehicle dynamics problems.


### [Project 1 — Launch Readiness & Structural Load Checks](./Project%201)

Two decision-support scripts:

- **Rocket Launch Checker** (`rocket_main.py`, `launch_checks.py`) — Evaluates go/no-go launch status based on weather conditions and system readiness, flagging the specific cause of any hold.
- **Beam Stress Checker** (`beam_main.py`, `beam_utils.py`) — Calculates maximum bending stress on a loaded beam and verifies it against allowable stress limits.

**Stack:** Python

**Run it:**
```bash
python rocket_main.py
python beam_main.py
```

**Sample output (Rocket Launch Checker):**
```
launch approved
launch hold
warning: weather outside limits.
launch hold
warning: systems not ready.
launch hold
warning: weather outside limits.
warning: systems not ready.
```

**Sample output (Beam Stress Checker):**
```
23999999.999999993
pass
47999999.999999985
fail
exceeds by: 17999999.999999985 Pa
```

### [Project 2 — Flight Route & Fuel Optimizer](./project_2)

- **Route Analysis** (`flight_main.py`, `trajectory_utils.py`) — Computes ground speed, flight time, and fuel consumption across multi-leg routes under varying wind conditions, classifies wind severity, and identifies the optimal route by distance, time, and fuel efficiency.

**Stack:** Python

**Run it:**
```bash
python flight_main.py
```

**Sample output:**
```
Monday route:
Total distance: 385.85 km
Total flight time: 2.04 h
Total fuel needed: 96.87 l/h

Recommendations
Shortest distance: 385.85 km (Monday)
Shortest flight time: 1.87 h (Tuesday)
Lowest fuel consumption: 89.99 liters (Tuesday)
```

### [Project 3 — Bridge Deflection Analysis](./Project_3)

- **Deflection Model** (`bridge_main.py`, `bridge_utils.py`) — Models a bridge under time-varying traffic loads and evaluates four structural cross-section designs using beam moment-curvature theory and numerical integration to determine which minimizes deflection.

**Stack:** NumPy, SciPy

**Run it:**
```bash
pip install numpy scipy
python bridge_main.py
```
*Requires a `traffic_loads.npy` input file with load data in the same directory.*

### [Project 4 — Quarter-Car Suspension Simulator](./Project_4)

- **Suspension Model** (`suspension_main.py`, `suspension_utils.py`) — Simulates a quarter-car suspension system (body mass, wheel mass, springs, dampers) across four road profiles using ODE integration, comparing four suspension tunings (Comfort, Sport, Off-road, Race) by ride smoothness (RMS acceleration) and control (max displacement).

**Stack:** NumPy, SciPy (`solve_ivp`)

**Run it:**
```bash
pip install numpy scipy
python suspension_main.py
```

**Sample output (Speed Bump profile):**
```
Road Profile: Speed Bump
Comfort   : rms_val = 2.0444 m/s^2, max_displacement = 24.39 mm
Sport     : rms_val = 1.8998 m/s^2, max_displacement = 29.85 mm
Off-road  : rms_val = 1.8567 m/s^2, max_displacement = 25.31 mm
Race      : rms_val = 2.0663 m/s^2, max_displacement = 36.57 mm
```

---

Built in VS Code with GitHub Copilot assistance.
