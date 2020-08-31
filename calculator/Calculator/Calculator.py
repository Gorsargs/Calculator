def spliter(text1):
    if len(text1) > 0:
        try:
            if type(text1) == str:
                text = ""
                for i in text1:
                    if i == " ":
                        continue
                    else:
                        text+= i
                num = "-+*/^√"
                number = "0123456789"
                parentheses = "()"
                tmp = ""
                for i in range(len(text)):
                    if i!= len(text)-1 and (text[i] == ")" and not(text[i+1] == "(")):
                        tmp += (f" {text[i]} ")
                    elif i!= len(text)-1 and (text[i] == ")" and text[i+1] == "("):
                        tmp += (f"{text[i]} *")
                    elif text[i] == ")" or text[i] == "(":
                        tmp += (f" {text[i]} ")
                    elif text[i] == "√":
                        if i!= 0 and text[i-1] == ")":
                            tmp+= f" * {text[i]} "
                        else:
                            tmp += (f" {text[i]} ")
                    elif text[i] == "^":
                        tmp += (f" {text[i]} ")
                    elif text[i] == "/":
                        tmp += (f" {text[i]} ")
                    elif text[i] == "%":
                        if i!= 0 and i != len(text)-1:
                            if text[i-1] in number and text[i+1] in number:
                                tmp += (f" {text[i]} * ")
                            elif text[i-1] in number and not(text[i+1] in number) and not(text[i+1] in parentheses):
                                tmp += (f" {text[i]} ")
                            elif text[i-1] == "(" and text[i+1] == ")":
                                tmp += f""
                            elif text[i-1] == ")" and text[i+1] == "(":
                                tmp += f" {text[i]} * "
                            elif text[i-1] == ")" and text[i+1] in number:
                                tmp += f" {text[i]}  "
                            elif text[i+1] == "(":
                                tmp += f" {text[i]} * "
                            elif text[i+1] == "√":
                                tmp += f" {text[i]} * "
                            elif text[i+1] == "^":
                                tmp += f" {text[i]} "
                        elif i == 0:
                            tmp += (f"0  {text[i]} ")
                        elif i == len(text)-1:
                            tmp += f" {text[i]}"

                    elif text[i] in num and i == 0 and (text[i] == "-" or text[i] == "+"):
                        if text[i+1] == "-":
                            tmp += (f"0 {text[i]} ")
                        elif text[i+1] == "+":
                            tmp += (f"0 {text[i]} ")
                        else:
                            tmp += (f"{text[i]}")
                    elif text[i] == "+" and text[i-1] == "e":
                        tmp+= (f"{text[i]}")
                    elif text[i] in num and i != 0 and (text[i-1] in num) and not(text[i-1] in parentheses):
                        tmp += (f"{text[i]}")
                    elif text[i] in num and i != 0 and not(text[i-1] in num) and not(text[i-1] in parentheses):
                        tmp += (f" {text[i]} ")
                    elif text[i] in num and i != 0  and (text[i] == "+" or text[i] == "-"):
                        if  text[i-1] in parentheses:
                            tmp+= (f" {text[i]} ")
                        elif text[i-1] in num:
                            tmp += (f"{text[i]}")
                    elif not(text[i] in num):
                        if i != len(text)-1 and (text[i+1] in parentheses or text[i-1] in parentheses):
                            if text[i+1] == "(" and text[i-1] == ")":
                                if i != 0:
                                    tmp += f" * {text[i]} * "
                                else:
                                    tmp += f"{text[i]} *"
                            elif text[i-1] == "(":
                                tmp += f"{text[i]}"
                            elif text[i+1] == ")":
                                tmp += f"{text[i]}"
                            elif text[i+1] == "(":
                                tmp += f"{text[i]} *"
                            elif text[i-1] == ")":
                                tmp += f"* {text[i]}"
                        elif i!= len(text)-1 and text[i+1] == "√":
                            tmp += f"{text[i]} *"
                        elif i == len(text)-1 and text[i-1] == ")":
                            tmp += f"* {text[i]}"
                        else:
                            tmp += f"{text[i]}"

                my_list = tmp.split()
                for i in range(len(my_list)):
                    try:
                        #transforming all possible str(numbers) to float
                        my_list[i] = float(my_list[i])
                    except:
                        pass
            return my_list

        except:
            print("please enter the str object")


def percent(text,i):
    text[i-1] *= 0.01
    text.remove(text[i])
    return text

def multiply(text,i):
    key = text[i-1] * text[i+1]
    text[i-1] = key
    text.remove(text[i+1])
    text.remove(text[i])
    return text


def devide(text,i):
    key = text[i-1] / text[i+1]
    text.remove(text[i+1])
    text[i-1] = key
    text.remove(text[i])
    return text


def plus(text,i):
    key = text[i-1] + text[i+1]
    text.remove(text[i+1])
    text[i-1] = key
    text.remove(text[i])
    return text

def minus(text,i):
    if i != 0:
        key = text[i-1] - text[i+1]
        text.remove(text[i+1])
        text[i-1] = key
        text.remove(text[i])
    elif i == 0 and type(text[i+1]) == float:
        text[i+1] = -(text[i+1])
        text.remove(text[i])
    return text

def square(text):
    result = []
    index = len(text)-1
    while text[index] != "^":
        index -=1
    i = index
    while text[i] == "^":
        key = text[i-1] ** text[i+1]
        text[i-1] = key
        text[i+1] = " "
        text[i] = " "
        i-=2
    text = [i for i in text if i != " "]
    return text

def root(text,i):
    key = text[i+1] ** 0.5
    text.remove(text[i+1])
    text[i] = key
    return text

def calculator_in(text):
    while ("%" in text):
        for i in range(len(text)):
            if text[i] == "%":
                text = percent(text,i)
                break
    while ("^" in text) or ("√" in text):
        for i in range(len(text)):
            if text[i] == "^":
                text = square(text)
                break
        for i in range(len(text)):
            if text[i] == "√" and type(text[i+1]) == float:
                text = root(text,i)
                break
    while ("*" in text) or ("/" in text):
        for i in range(len(text)):
            if text[i] == "*":
                text = multiply(text,i)
                break
            elif text[i] == "/":
                text  = devide(text,i)
                break
    while ("+" in text) or ("-" in text):
        for i in range(len(text)):
            if text[i] == "+":
                text = plus(text,i)
                break
            elif text[i] == "-":
                text = minus(text,i)
                break
    #print(text)
    return text

def calculator(text):
    try :
        text1 = "".join([str(i) for i in spliter(text)])
        x = 0
        while text1.count("(") != 0:
            for i in range(len(text1)):
                if text1[i] == "(":
                    j = i
                if text1[i] == ")":
                    x = i
                    break
            text1 = text1.replace(text1[j:x+1],str(calculator_in(spliter(text1[j+1:x]))[0]))
        result = calculator_in(spliter(text1))
        print(result[0])
        return str(result[0])
    except:
        print("please input the valid number")
