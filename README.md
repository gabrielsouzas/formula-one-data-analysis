# 🏎️ FastF1 Study Repository

This repository is dedicated to learning, experimenting, and documenting my studies with the **[FastF1](https://theoehrly.github.io/Fast-F1/)** library.

FastF1 is a Python library that provides access to Formula 1 lap timing, car telemetry, tyre data, weather data, event schedules, and session results. It is designed for F1 enthusiasts and data nerds who want to analyze Formula 1 races using Python.

---

## 📌 About FastF1

Main features of FastF1 include:

- Access to **F1 timing data, telemetry, session results, and more**
- Full support for the **Ergast-compatible jolpica-f1 API** for current and historical F1 data
- Data is provided as **extended Pandas DataFrames**, making it easier to work with while keeping powerful tools available
- **Custom Pandas functions** for F1 data
- **Matplotlib integration** for visualization
- **Built-in caching** to speed up repeated API requests

---

## 🚀 Installation

You can install FastF1 using **pip**:

```bash
pip install fastf1
```

Or using **conda**:

```bash
conda install -c conda-forge fastf1
```

> ⚠️ Python 3.8 or higher is required.

---

## 💿 Virtual Enviorement

```shell
py -m venv .
.\Scripts\Activate.ps1
```

---

## 💾 Install other dependencies

```shell
pip install -r requirements.txt
```

---

## 📊 Available Data

With FastF1 you can access:

- **Event schedule** (dates, times, countries, locations, etc.)
- **Results** (driver names, teams, positions, points, finishing status, etc.)
- **Timing data** (lap times, sector times, pit stops, tyre usage, etc.)
- **Telemetry** (speed, RPM, gear, throttle, brake, track position, etc.)
- **Track status & session status** (flags, safety cars, session started/finished)
- **Race control messages** (penalties, investigations, restarts, etc.)
- **Historical data** via the **Ergast API** (going back to 1950)

---

## 🎯 Purpose of This Repository

This repository is not an official project, but rather a **study environment** to:

- Explore **FastF1 features and APIs**
- Build **example scripts** for data analysis and visualization
- Document **learning progress** and key insights
- Experiment with **Formula 1 analytics** using Python

---

## 📂 Repository Structure (planned)

```
📦 fastf1-studies
 ┣ 📜 README.md          → Documentation of this repo
 ┣ 📂 examples           → Scripts with FastF1 usage examples
 ┣ 📂 notebooks          → Jupyter notebooks with step-by-step studies
 ┣ 📂 docs               → Notes, summaries, and useful references
```

---

## ⚠️ Notice

This repository is **unofficial** and not affiliated with Formula 1 or the maintainers of FastF1.
All F1 trademarks are owned by **Formula One Licensing B.V.**

---

## 📚 References

- 📖 [FastF1 Documentation](https://theoehrly.github.io/Fast-F1/)
- 📦 [FastF1 on PyPI](https://pypi.org/project/fastf1/)
- 📂 [FastF1 GitHub Repository](https://github.com/theOehrly/Fast-F1)
