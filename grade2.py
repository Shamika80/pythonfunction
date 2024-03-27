def calculate_average_grade(grades):
  

  if not grades:
    return None

  total_grade = sum(grades)
  average_grade = total_grade / len(grades)
  return average_grade

def find_highest_and_lowest(grades):
 

  if not grades:
    return None

  highest_grade = max(grades)  # Corrected line
  lowest_grade = min(grades)
  return highest_grade, lowest_grade

# Example usage (assuming you have a list of grades)
grades = [85, 92, 78, 90, 82]
average_grade = calculate_average_grade(grades)
highest, lowest = find_highest_and_lowest(grades)

if average_grade is not None:
  print(f"The average grade is: {average_grade:.2f}")
  print(f"The highest grade is: {highest}")
  print(f"The lowest grade is: {lowest}")
else:
  print("The list of grades is empty.")