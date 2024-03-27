def log_fitness_activity(activities, durations):
  
  if len(activities) != len(durations):
    raise ValueError("Error: The number of activities and durations must be equal.")

  activity_log = {}
  for i, activity in enumerate(activities):
    activity_log[activity] = durations[i]

  return activity_log