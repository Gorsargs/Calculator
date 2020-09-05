[1mdiff --git a/calculator/Calculator/Calculator.py b/calculator/Calculator/Calculator.py[m
[1mindex 99e0a5c..2fb4d19 100644[m
[1m--- a/calculator/Calculator/Calculator.py[m
[1m+++ b/calculator/Calculator/Calculator.py[m
[36m@@ -7,7 +7,7 @@[m [mdef spliter(text1):[m
                     if i == " ":[m
                         continue[m
                     else:[m
[31m-                        text+= i[m
[32m+[m[32m                        text += i[m
                 num = "-+*/^√"[m
                 number = "0123456789"[m
                 parentheses = "()"[m
[36m@@ -19,6 +19,8 @@[m [mdef spliter(text1):[m
                         tmp += (f"{text[i]} *")[m
                     elif text[i] == ")" or text[i] == "(":[m
                         tmp += (f" {text[i]} ")[m
[32m+[m[32m                    elif text[i-1] == "(" and text[i+1] == ")":[m
[32m+[m[32m                        tmp += (f" {text[i]} ")[m
                     elif text[i] == "√":[m
                         if i!= 0 and text[i-1] == ")":[m
                             tmp+= f" * {text[i]} "[m
[36m@@ -47,7 +49,7 @@[m [mdef spliter(text1):[m
                             elif text[i+1] == "^":[m
                                 tmp += f" {text[i]} "[m
                         elif i == 0:[m
[31m-                            tmp += (f"0  {text[i]} ")[m
[32m+[m[32m                            tmp += (f" 0  {text[i]} ")[m
                         elif i == len(text)-1:[m
                             tmp += f" {text[i]}"[m
 [m
[36m@@ -71,7 +73,7 @@[m [mdef spliter(text1):[m
                             tmp += (f"{text[i]}")[m
                     elif not(text[i] in num):[m
                         if i != len(text)-1 and (text[i+1] in parentheses or text[i-1] in parentheses):[m
[31m-                            if text[i+1] == "(" and text[i-1] == ")":[m
[32m+[m[32m                            if i!= 0 and (text[i+1] == "(" and text[i-1] == ")"):[m
                                 if i != 0:[m
                                     tmp += f" * {text[i]} * "[m
                                 else:[m
[36m@@ -82,16 +84,17 @@[m [mdef spliter(text1):[m
                                 tmp += f"{text[i]}"[m
                             elif text[i+1] == "(":[m
                                 tmp += f"{text[i]} *"[m
[31m-                            elif text[i-1] == ")":[m
[31m-                                tmp += f"* {text[i]}"[m
[32m+[m[32m                            elif text[i-1] == ")" :[m
[32m+[m[32m                                tmp += f" * {text[i]} "[m
                         elif i!= len(text)-1 and text[i+1] == "√":[m
[31m-                            tmp += f"{text[i]} *"[m
[31m-                        elif i == len(text)-1 and text[i-1] == ")":[m
[31m-                            tmp += f"* {text[i]}"[m
[32m+[m[32m                            tmp += f" {text[i]} *"[m
[32m+[m[32m                        elif  i == len(text)-1 and text[i-1] == ")":[m
[32m+[m[32m                            tmp += f" * {text[i]} "[m
                         else:[m
                             tmp += f"{text[i]}"[m
 [m
                 my_list = tmp.split()[m
[32m+[m
                 for i in range(len(my_list)):[m
                     try:[m
                         #transforming all possible str(numbers) to float[m
[36m@@ -110,9 +113,8 @@[m [mdef percent(text,i):[m
     return text[m
 [m
 def multiply(text,i):[m
[31m-    key = text[i-1] * text[i+1][m
[31m-    text[i-1] = key[m
[31m-    text.remove(text[i+1])[m
[32m+[m[32m    text[i-1] = text[i-1] * text[i+1][m
[32m+[m[32m    text.remove(text[i])[m
     text.remove(text[i])[m
     return text[m
 [m
[1mdiff --git a/calculator/Calculator/__pycache__/Calculator.cpython-38.pyc b/calculator/Calculator/__pycache__/Calculator.cpython-38.pyc[m
[1mindex bea30c2..19bd5e9 100644[m
Binary files a/calculator/Calculator/__pycache__/Calculator.cpython-38.pyc and b/calculator/Calculator/__pycache__/Calculator.cpython-38.pyc differ
[1mdiff --git a/calculator/__pycache__/main.cpython-38.pyc b/calculator/__pycache__/main.cpython-38.pyc[m
[1mindex 43e5ac4..5a13c2c 100644[m
Binary files a/calculator/__pycache__/main.cpython-38.pyc and b/calculator/__pycache__/main.cpython-38.pyc differ
