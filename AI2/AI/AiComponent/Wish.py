import datetime

def wish_me():
    try:
        intro = "i am jarvis, how can i help you"
        hour = int (datetime.datetime.now().hour)
        if hour > 6 and hour < 12:
            wish = "Good morning sir"
        elif hour >= 12 and hour < 18:
            wish = "Good afternoon sir"
        else:
            wish = "Good evening sir"
        return wish,intro
    except Exception as e:
        print(e)