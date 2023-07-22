from main import question_bank
question_number = 0
class QuizBrain:
    def __init__(self,question_number) -> None:
        print("")

    def next_question(self,question_number):
        self.next_question=question_bank[question_number]

answer = input()
q = QuizBrain(1)
