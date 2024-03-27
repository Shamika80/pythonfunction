def summarize_activity_log(activity_log):

  total_calories_burned = 0
  print("Activity Summary:")
  for activity, duration in activity_log.items():
    calories_burned = "estimate_calories_burned"(activity, duration)
    total_calories_burned += calories_burned
    print(f"{activity}: {duration} minutes ({calories_burned} calories burned)")

  print(f"Total calories burned: {total_calories_burned} calories")

activities = ["Running", "Swimming", "Yoga"]
durations = [30, 20, 45]

activity_log = "log_fitness_activity"(activities, durations)
summarize_activity_log(activity_log)