from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

playing = True

quiz = QuizBrain(question_bank)
score = 0
question_count = 0
while playing and question_count <= len(question_bank)-1:
    question_count +=1
    response = quiz.next_question()
    if quiz.check_answer(response):
        score += 1
        print("You got it right!")
        print(f"The correct answer was: {response}")
        print(f"Your current score is {score}/{question_count}")
    else:
        print("Incorrect answer!")

