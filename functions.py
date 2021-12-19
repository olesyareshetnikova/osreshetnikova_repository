import re


def read(n):
    with open(n, 'r') as f:
        line = ''
        for i in f:
            line = line + i + ' '
    line.strip()
    line = re.sub(r'\s+', ' ', line)
    line = re.sub(r'(\n|\t)', ' ', line)
    line = line.split(' ')
    if line[0] == '':
        bot_line = 1
    else:
        bot_line = 0
    if line[-1] == '':
        upper_bound = len(line) - 1
    else:
        upper_bound = len(line)
    line = line[bot_line:upper_bound]
    for i in line:
        try:
            value = float(i)
        except Exception:
            return "Incorrect"
    for i in range(len(line)):
        if '.' in line[i]:
            line[i] = float(line[i])
        else:
            line[i] = int(line[i])
    return line


def maximum(line):
    if line != "Incorrect":
        maxim = line[0]
        for element in line:
            if element > maxim:
                maxim = element
        return maxim
    else:
        return "Incorrect"


def minimum(line):
    if line != "Incorrect":
        minim = line[0]
        for element in line:
            if element < minim:
                minim = element
        return minim
    else:
        return "Incorrect"


def prod_of_numbers(line):
    if line != "Incorrect":
        try:
            answ = 1
            for i in range(0, len(line)):
                answ = answ * line[i]
            return answ
        except OverflowError:
            return "OverflowError"
    else:
        return "Incorrect"


def summation(line):
    if line != "Incorrect":
        sum_number = 0
        for number in line:
            sum_number += number
        return sum_number
    else:
        return "Incorrect"
