from greeting import greeting_the_user
from question import get_random_question, ask_question
from storage import record_response, show_summary

while True:
    def run_survey():
        greeting_the_user()
        questions = get_random_question(3)
        for i, question in enumerate(questions, 1):
            print(f"Question {i}/3:")
            answer = ask_question(question)
            record_response(question, answer)
            print("Answer recorded")
        show_summary()

    if __name__== "__main__":
        run_survey()