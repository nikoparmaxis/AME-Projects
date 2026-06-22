# AME-Projects

Engineering analysis and simulation scripts built in Python, applying numerical methods to structural, aerospace, and dynamics problems. Developed for coursework, using NumPy and SciPy for modeling and analysis.


### Project 1 — Launch Readiness & Structural Load Checks
Two decision-support scripts:
- **Rocket Launch Checker** (`rocket_main.py`, `launch_checks.py`) — Evaluates go/no-go launch status based on weather conditions and system readiness, flagging the specific cause of any hold.
- **Beam Stress Checker** (`beam_main.py`, `beam_utils.py`) — Calculates maximum bending stress on a loaded beam and verifies it against allowable stress limits.

**Stack:** Python

### Project 2 — Flight Route & Fuel Optimizer
Analyzes multi-leg flight routes under varying wind conditions to compute ground speed, flight time, and fuel consumption. Classifies wind severity and applies corresponding fuel penalties, then identifies the optimal route by distance, time, and fuel efficiency.

**Stack:** Python

### Project 3 — Bridge Deflection Analysis
Models a bridge under time-varying traffic loads and evaluates four structural cross-section designs to determine which minimizes deflection. Applies beam moment-curvature theory with numerical integration to simulate load response across the span.

**Stack:** NumPy, SciPy

### Project 4 — Quarter-Car Suspension Simulator
Simulates a quarter-car suspension model (body mass, wheel mass, springs, dampers) across four road profiles using ODE integration. Compares four suspension tunings (Comfort, Sport, Off-road, Race) by ride smoothness (RMS acceleration) and control (max displacement).

**Stack:** NumPy, SciPy (`solve_ivp`)

---

Built in VS Code with GitHub Copilot assistance.

