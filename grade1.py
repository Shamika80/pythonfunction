def calculate_average_grade(grades):
 
  if not grades:
    return None

  total_grade = sum(grades)
  average_grade = total_grade / len(grades)
  return average_grade

grades = [85, 92, 78, 90, 82]
average_grade = calculate_average_grade(grades)

if average_grade is not None:
  print(f"The average grade is: {average_grade:.2f}")
else:
  print("The list of grades is empty.")