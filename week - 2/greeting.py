import datetime

def greeting_the_user():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    print(f"\n{greeting}! Welcome to our survey \nWe'll ask you a few questions to get your opinions \nLet get started")