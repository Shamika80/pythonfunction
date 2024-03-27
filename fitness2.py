def estimate_calories_burned(activity, duration, METs=3.5):


  # Avoid negative or zero duration
  if duration <= 0:
    return 0

  # Calculate estimated calories burned
  calories_burned = duration * METs

  return int(calories_burned)