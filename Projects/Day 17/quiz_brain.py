class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list

    def next_question(self):
        self.question_number += 1
        self.text = self.questions_list[self.question_number-1].text
        #current_question.text
        #input(f"Q. {self.question_number} {questions_list[self.question_number]} (True/False)")
        question = input(f"Q. {self.question_number} {self.text} (True/False)?: ").lower()
        return question

    def check_answer(self, response):
        if response == self.questions_list[self.question_number-1].answer.lower():
            return True
        else:
            return False


