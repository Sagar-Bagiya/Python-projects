
def read_data(quary):
    with open("my file.txt", "r") as f:
        data = f.readlines()
        mod = False
        for line in data:
            if mod is True:
                line = line.replace("\n", "")
                return line
            if quary in line:
                mod = True

def write_data(question, answer):
    with open("my file.txt", "a") as f:
        f.write("\n")
        f.write(question)
        f.write("\n")
        f.write(answer)