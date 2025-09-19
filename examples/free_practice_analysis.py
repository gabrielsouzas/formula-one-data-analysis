import fastf1
import pandas as pd

# Enable cache
# fastf1.Cache.enable_cache('cache')

# Load session (Free Practice 2 of Bahrain GP 2023 as example)
session = fastf1.get_session(2025, 'Azerbaijan', 'FP2')
session.load()

# Collect results
results = []

for drv in session.drivers:
    laps = session.laps.pick_driver(drv).pick_quicklaps()  # remove in/out laps
    if laps.empty:
        continue

    # Best sectors
    best_s1 = laps['Sector1Time'].min()
    best_s2 = laps['Sector2Time'].min()
    best_s3 = laps['Sector3Time'].min()

    # Ideal lap = sum of best sectors
    ideal_lap = best_s1 + best_s2 + best_s3

    # Best actual lap
    best_lap = laps['LapTime'].min()

    results.append({
        "Driver": session.get_driver(drv)['Abbreviation'],
        "Best Lap": best_lap.total_seconds(),
        "Ideal Lap": ideal_lap.total_seconds(),
        "Delta (Ideal - Best)": (ideal_lap - best_lap).total_seconds()
    })

# Convert to DataFrame
df = pd.DataFrame(results)

# Sort by ideal lap
df = df.sort_values("Ideal Lap").reset_index(drop=True)

print(df)

# Optionally, export to CSV
df.to_csv("fp2_analysis.csv", index=False)
