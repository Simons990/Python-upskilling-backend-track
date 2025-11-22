import datetime
all_responses = []
def record_response(question, answer):
    timestamp = datetime.datetime.now()
    response = {
        "timestamp": timestamp,
        "question": question["text"],
        "answer": answer,
        "question_type": question["type"]
    }
    all_responses.append(response)
    return response

def show_summary():
    print("     Survey Summary     ")

    for i, response in enumerate(all_responses, 1):
        time_str = response["timestamp"].strftime("%H:%M:%S")
        print(f"{i}. [{time_str}] {response['question']}")
        print(f"   Answer: {response['answer']}")

    print(f"\nTotal responses: {len(all_responses)}")
    print("Thank you for completing the survey!")