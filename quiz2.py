def take_quiz(questions):
  score = 0
  for question in questions:
    answer = input(f"{question['question']}: ")
    if answer.lower() == question["answer"].lower():
      print("Correct!")
      score += 1
    else:
      print(f"Incorrect. The answer is: {question['answer']}")
  print(f"You scored {score} out of {len(questions)} questions.")


questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the tallest mountain in the world?", "answer": "Mount Everest"},
    {"question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean"},
    {"question": "What year did World War II end?", "answer": "1945"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
]

take_quiz(questions)