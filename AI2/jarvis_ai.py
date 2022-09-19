import AI
jarvis = AI.myAi()

Ai_runing = False
# jarvis.wish_me()

def main(user_command):

    user_command = user_command.lower()

    if "open" in user_command:
        if "open notepad" in user_command:
            jarvis.open.notepad()
            jarvis.speak("sir, your notepad is ready to use!")

        elif "open youtube" in user_command:
            jarvis.speak("yes sir")
            jarvis.speak("sir,what should i search on youtube")
            jarvis.open.youtube(jarvis.listen())

        elif "open mozilla" in user_command:
            jarvis.open.mozilla()
            jarvis.speak("boss, your mozila is hear")

        elif "open chorme" in user_command:
            jarvis.open.chrome()
            jarvis.speak("boss, your chorme is hear")

        elif "open google" in user_command:
            jarvis.speak("yes sir")
            jarvis.speak("sir what should i search on google")
            user_command = jarvis.listen()
            user_command = user_command.lower()
            jarvis.open.google(user_command)  

    elif "virtual display" in user_command :
        while True :
            jarvis.speak('ok sir, i am activating virtual display command, ok now give me command!')
            user_command = jarvis.listen()
            if 'close' in user_command :
                break
            else :
                if not jarvis.disText_command(user_command, 3) :
                    main(user_command)

    elif "virtual mouse" in user_command :
        jarvis.speak('okay sir!, i am activating virtual mouse mod!')
        jarvis.virtual_mouse()

    elif ("according to wikipedia" or "in wikipedia") in user_command:
        jarvis.speak("yes sir")
        user_command = user_command
        user_command = user_command.replace("according to wikipedia", "?")
        user_command = user_command.replace("in wikipedia", "?")
        jarvis.speak("according to wikipedia," + jarvis.open.wikipedia(user_command))

    elif "+" in user_command:
        jarvis.speak("yes sir")
        jarvis.math.add(user_command)

    elif "-" in user_command:
        jarvis.speak("yes sir")
        jarvis.math.sub(user_command)

    elif "x" in user_command:
        jarvis.speak("yes sir")
        jarvis.math.mul(user_command)

    elif "/" in user_command:
        jarvis.speak("yes sir")
        jarvis.math.add(user_command)

    elif "shutdown" in user_command:
        jarvis.speak("ok sir,i enjoyed talking with you!, have a good day!")
        Ai_runing = False
  
def ifJarvis(user_command):

    type_of_commands = []

    if 'jarvis' in user_command:

        if ' jarvis ' in user_command:
            greet, user_command = user_command.split(' jarvis ')
            # print(greet, user_command)
            type_of_command1 = jarvis.Query_analysis(greet)
            type_of_command2 = jarvis.Query_analysis(user_command)
            # print(type_of_command1,type_of_command2)
            type_of_commands = [type_of_command1, type_of_command2]

        elif ' jarvis' in user_command :
            user_command = user_command.replace('jarvis', "")
            # print(user_command)
            type_of_command = jarvis.Query_analysis(user_command)
            # print(type_of_command)
            type_of_commands = [type_of_command]

        else :
            user_command = user_command.replace('jarvis ', "")
            # print(user_command)
            type_of_command = jarvis.Query_analysis(user_command)
            # print(type_of_command)
            type_of_commands = [type_of_command]

        # print(type_of_commands)
        # ACTION
        for type_of_command in type_of_commands:
            if type_of_command[2] == "udagar":
                print("udagar")

            elif type_of_command[2] == "command":
                command = str(type_of_command[0][0]) + " " + str(type_of_command[1][0])
                # print("command")
                # print(command)
                main(command)

            elif type_of_command[2] == "Interrogative":
                # user_command = type_of_command[0]
                print("Interrogative")
                # print(user_command)


while Ai_runing:
    user_command = jarvis.listen()
    ifJarvis(user_command)

user_command = "jarvis virtual mouse"
# jarvis.disText_command('help', 3)
ifJarvis(user_command)