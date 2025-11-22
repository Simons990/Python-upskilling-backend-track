import random

question_pool =[
    {"text": "What's your name?", "type": "open"},
    {"text": "Which country is winning the world cup?", "type": "multiple", "options": ["1. Brazil","2. Portugal", "3. USA", "4. Spain", "5. Ghana"]},
    {"text": "Who is the GOAT (A/B/C)", "type": "multiple", "options": ["1. Ronaldo", "2. Messi", "3. Neymar"]},
    {"text": "What's your favorite hobby?", "type": "open"},
    {"text": "Rate your day from 1-10:", "type": "range", "options": [str(i) for i in range(1, 11)]}
]
def get_random_question(num_questions=3):
    return random.sample(question_pool, num_questions)
def ask_question(question_info):
    question_text = question_info["text"]
    question_type = question_info["type"]
    while True:
        print(f"Q: {question_text}")
        if question_type in ["multiple", "range"]:
            options = question_info["options"]
            if "Rate your day" in question_text:
                print(f"Options: {', '.join(options)}")
            else:
                print("  Options  ")
                for option in options:
                    print(f"  {option}")
        answer = input("Your answer: ").strip()
        if correct_input(answer, question_info):
            return format_answer(answer, question_info)
        else:
            print("Invalid input. Please try again.\n")
def correct_input(answer, question_info):
    question_type = question_info["type"]
    if not answer:
        print("Please provide an answer.")
        return False
    if question_type in ["multiple", "range"]:
        options = question_info["options"]
        valid_numbers = [str(i) for i in range(1, len(options) + 1)]
        if answer not in valid_numbers:
            print(f"Please choose a number from 1 to {len(options)}")
            return False
    return True
def format_answer(answer, question_info):
    question_type = question_info["type"]
    if question_type == ["multiple","range"]:
        options = question_info["options"]
        index = int(answer) - 1
        return options[index]
    else:
        return answer