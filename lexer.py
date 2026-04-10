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
    ("Character",            r"'[^'\\]'|'\\.'"),
    ("String",               r'"[^"]*"'),
    ("Number",               r'[0-9]+(\.[0-9]+)?'),
    ("Relational Operator",  r'==|!=|<=|>=|<|>'),
    ("Assignment Operator",  r'\+=|-=|\*=|/=|%=|='),
    ("Logical Operator",     r'&&|\|\||!'),
    ("Arithmetic Operator",  r'\+\+|--|[+\-*/%]'),
    ("Symbol",               r'[(){}\[\],;:]'),
    ("Word",                 r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ("1D Vector", r'vector\s*<\s*\w+\s*>\s*\w+\s*(\([^)]*\)|\{[^}]*\}|=\s*\{[^}]*\})?'),
]

with open("input.txt", "r") as f:
    code = f.read()

with open("output.txt", "w") as fout:
    i = 0
    while i < len(code):
        if code[i] in ' \t\n':
            i += 1
            continue

        matched = False
        for token_type, pattern in patterns:
            m = re.match(pattern, code[i:])
            if m:
                word = m.group(0)
                if token_type == "Library":
                    fout.write(f"Library : {m.group(1)}\n")
                elif token_type == "Word":
                    if word in keywords:
                        fout.write(f"Keyword : {word}\n")
                    else:
                        rest = code[i + len(word):].lstrip()
                        if rest and rest[0] == '(':
                            end = code.index(')', i) + 1
                            fout.write(f"Function : {code[i:end]}\n")
                            i = end
                            matched = True
                            continue
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

print("Check output.txt")
