# AME-Projects

Engineering analysis and simulation scripts built in Python, applying numerical methods to structural, aerospace, and dynamics problems. Developed for coursework, using NumPy and SciPy for modeling and analysis.


## Project 1 — Launch Readiness & Structural Load Checks

Two decision-support scripts:

- **Rocket Launch Checker** (`rocket_main.py`, `launch_checks.py`) — Evaluates go/no-go launch status based on weather conditions and system readiness, flagging the specific cause of any hold.
- **Beam Stress Checker** (`beam_main.py`, `beam_utils.py`) — Calculates maximum bending stress on a loaded beam and verifies it against allowable stress limits.

**Stack:** Python

## Project 2 — Flight Route & Fuel Optimizer

- **Route Analysis** (`flight_main.py`, `trajectory_utils.py`) — Computes ground speed, flight time, and fuel consumption across multi-leg routes under varying wind conditions, classifies wind severity, and identifies the optimal route by distance, time, and fuel efficiency.

**Stack:** Python

## Project 3 — Bridge Deflection Analysis

- **Deflection Model** (`bridge_main.py`, `bridge_utils.py`) — Models a bridge under time-varying traffic loads and evaluates four structural cross-section designs using beam moment-curvature theory and numerical integration to determine which minimizes deflection.

**Stack:** NumPy, SciPy

## Project 4 — Quarter-Car Suspension Simulator

- **Suspension Model** (`suspension_main.py`, `suspension_utils.py`) — Simulates a quarter-car suspension system (body mass, wheel mass, springs, dampers) across four road profiles using ODE integration, comparing four suspension tunings (Comfort, Sport, Off-road, Race) by ride smoothness (RMS acceleration) and control (max displacement).

**Stack:** NumPy, SciPy (`solve_ivp`)

---

Built in VS Code with GitHub Copilot assistance.
