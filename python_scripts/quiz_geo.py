import random

# List of questions and answers
questions = [
    ("What is the capital of France?", "Paris"),
    ("What is the largest country in the world?", "Russia"),
    ("What is the longest river in the world?", "Nile"),
    ("What is the highest mountain in the world?", "Mount Everest"),
    ("What is the driest place on Earth?", "Atacama Desert"),
]

# Shuffle the questions
random.shuffle(questions)

# Start the quiz
score = 0
for question, answer in questions:
  # Ask the question
  user_answer = input(question + " ")
  
  # Check the answer
  if user_answer.lower() == answer.lower():
    score += 1
    print("Correct!")
  else:
    print("Incorrect. The correct answer is " + answer + ".")

# Print the final score
print("You scored " + str(score) + " out of " + str(len(questions)) + ".")
#This code defines a list of geography questions and answers and shuffles them using the random module. It then asks the questions one by one and checks the user's answers. If the answer is correct, it increments the score. At the end, it prints the final score.

#You can customize the quiz by adding more questions and answers and changing the gameplay mechanics as needed. For example, you could add a timer to limit the amount of time the user has to answer each question, or you could add multiple choice options to make the quiz more challenging.




