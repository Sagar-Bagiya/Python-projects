def add(mystr):
    list = mystr.split(" ")
    ref = list.index("+")
    num1 = float(list[ref - 1])
    num2 = float(list[ref + 1])
    operation = str(num1 + num2)
    return operation
            
def sub(mystr):
    list = mystr.split(" ")
    ref = list.index("-")
    num1 = float(list[ref - 1])
    num2 = float(list[ref + 1])
    operation = str(num1 - num2)
    return operation

def mul(mystr):
    mystr = mystr.lower()
    list = mystr.split(" ")
    ref = list.index("x")
    num1 = float(list[ref - 1])
    num2 = float(list[ref + 1])
    operation = str(num1 * num2)
    return operation    

def division(mystr):
    list = mystr.split(" ")
    ref = list.index("/")
    num1 = float(list[ref - 1])
    num2 = float(list[ref + 1])
    operation = str(num1 / num2)
    return operation



