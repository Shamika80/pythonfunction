def take_quiz(questions):

  score = 0
  for question in questions:
    answer = input(f"{question['question']}: ")
    if answer.lower() == question["answer"].lower():
      print("Correct!")
      score += 1
    else:
      print(f"Incorrect. The answer is: {question['answer']}")
  total_questions = len(questions)
  percentage_score = (score / total_questions) * 100

  if percentage_score >= 90:
    feedback = "Excellent work!"
  elif percentage_score >= 70:
    feedback = "Good job!"
  elif percentage_score >= 50:
    feedback = "You can do better with some practice."
  else:
    feedback = "You might want to review the material."

  print(f"You scored {score} out of {total_questions} questions ({percentage_score:.2f}%).")
  print(feedback)

questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the tallest mountain in the world?", "answer": "Mount Everest"},
    {"question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean"},
    {"question": "What year did World War II end?", "answer": "1945"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
]

take_quiz(questions)