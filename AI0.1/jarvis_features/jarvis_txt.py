
def read_data(quary):

    try:
        with open("my file.txt", "r") as f:
            data = f.readlines()
            mod = False
            for line in data:
                if mod is True:
                    line = line.replace("\n", "")
                    return line
                if quary in line:
                    mod = True
    except Exception as e:
        print(e)
        return None
    return None

def write_data(question, answer):

    try:
        with open("my file.txt", "a") as f:
            f.write("\n")
            f.write(question)
            f.write("\n")
            f.write(answer)
    except Exception as e:
        print(e)
        return None
    return True

# def read_data(quary):
#     try:
#         with open("jarvis_question.txt", "r") as f:
#             data = f.readlines()
#             mod = False
#             for line in data:
#                 if quary in line:
#
#
#     except Exception as e:
#         print(e)
#         return None
#     return True