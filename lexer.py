import re

keywords = [
    "int","float","double","char","bool","void",
    "if","else","for","while","do","return",
    "break","continue","class","struct","switch",
    "case","public","private","static","const",
    "true","false"
]

patterns = [
    ("Library",              r'#include\s*[<"]([^>"]+)[>"]'),
    ("Single Line Comment",  r'//[^\n]*'),
    ("Multi Line Comment",   r'/\*[\s\S]*?\*/'),
    ("Character", r"'[^'\\]'|'\\.'"), #'a','1','\n'..... , .- any one(\n , \t...)
    ("String",               r'"[^"]*"'),
    ("Number",               r'[0-9]+(\.[0-9]+)?'),
    ("Relational Operator",  r'==|!=|<=|>=|<|>'),
    ("Assignment Operator",  r'\+=|-=|\*=|/=|%=|='),
    ("Logical Operator",     r'&&|\|\||!'),
    ("Arithmetic Operator",  r'\+\+|--|[+\-*/%]'),
    ("Symbol",               r'[(){}\[\],;:]'),
    ("Word",                 r'[a-zA-Z_][a-zA-Z0-9_]*'),
]

with open("input.txt", "r") as f:
    code = f.read()

with open("output.txt", "w") as fout:
    i = 0
    while i < len(code):

        # skip whitespace
        if code[i] in ' \t\n':
            i += 1
            continue

        matched = False

        for token_type, pattern in patterns:
            m = re.match(pattern, code[i:]) #p by p. 
            if m:
                word = m.group(0) #Entire matched text - '42' , 'int' .....

                if token_type == "Library":
                    fout.write(f"Library : {m.group(1)}\n")

                elif token_type == "Word":
                    if word in keywords:
                        fout.write(f"Keyword : {word}\n")
                    else:
                        rest = code[i + len(word):].lstrip()
                        if rest and rest[0] == '(':   #func.
                            fout.write(f"Function : {word}\n") 
                        else:
                            fout.write(f"Identifier : {word}\n")

                else:
                    fout.write(f"{token_type} : {word}\n")

                i += len(word)
                matched = True
                break

        if not matched:
            fout.write(f"Invalid Token : {code[i]}\n")
            i += 1

print("Done! Check output.txt")