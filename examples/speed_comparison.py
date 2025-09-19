import fastf1
import fastf1.plotting
from matplotlib import pyplot as plt

# Enable cache (improves performance on repeated runs)
# fastf1.Cache.enable_cache('cache')  # creates a "cache" folder in your project

# Load session (example: 2023 Bahrain GP Qualifying)
session = fastf1.get_session(2023, 'Bahrain', 'Q')
session.load()

# Pick two drivers for comparison
ver = session.laps.pick_driver('VER')  # Max Verstappen
lec = session.laps.pick_driver('LEC')  # Charles Leclerc

# Get fastest laps
ver_fastest = ver.pick_fastest()
lec_fastest = lec.pick_fastest()

# Get telemetry data for both drivers
ver_tel = ver_fastest.get_car_data().add_distance()
lec_tel = lec_fastest.get_car_data().add_distance()

# Plot comparison
plt.figure(figsize=(12, 6))
plt.plot(ver_tel['Distance'], ver_tel['Speed'], label='VER - Max Verstappen')
plt.plot(lec_tel['Distance'], lec_tel['Speed'], label='LEC - Charles Leclerc')

plt.title('Fastest Lap Speed Comparison - Bahrain GP 2023 (Qualifying)')
plt.xlabel('Distance (m)')
plt.ylabel('Speed (km/h)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
