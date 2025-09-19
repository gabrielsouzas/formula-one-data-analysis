import fastf1

schedule = fastf1.get_event_schedule(2025)

print(schedule[['RoundNumber', 'EventName', 'EventDate']])
