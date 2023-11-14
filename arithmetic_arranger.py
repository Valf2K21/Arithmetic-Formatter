'''
    The Arithmetic Formatter is a Python application written as partial requirement of freeCodeCamp's Scientific Computing with Python Certification.
    Written November 2023 by Valfrid Galinato
'''

# immport dependencies
import re

# create a function to arrange and solve basic math operations vertically
def arithmetic_arranger(problems: list[str], display_ans = False):
    # initialize list variables to store operands, symbols, and answers
    operand_set1 = []
    operand_set2 = []
    symbol_set = []
    answer_set = []

    # use re.compile() function to define a regex pattern and capture the math operands and symbol
    # note: each group is encapsulated in open and close parentheses
    pattern = re.compile(r'(\w{1,})\s*([\+\-\*\/])\s*(\w{1,})')

    # for-loop to loop through each problem in problems list
    for problem in problems:
        # if-statement to check if problems' length is more than 4
        if len(problems) > 5:
            # return error message
            return 'Error: Too many problems.'

        # use patter.match() function to use pattern variable in checking currently-iterated problem
        match = pattern.match(problem)

        # initialize list to store currently-iterated match's operands
        operands = []

        # if-statement to determine if any match is found
        if match:
            # append the two operands in operands list
            operands.append(match.group(1))
            operands.append(match.group(3))

            # for-loop to loop through contents of operands list
            for index, operand in enumerate(operands):
                # if-statement to check length of currently-iterated operand
                if len(operand) > 4:
                    # return error message
                    return 'Error: Numbers cannot be more than four digits.'
                
                # try-except block to attempt converting currently-iterated operand into int
                try:
                    # if-elif statement to determine where to append currently-iterated operand
                    if index == 0 and int(operand):
                        # append first operand to operand_set1 list
                        operand_set1.append(operand)

                    elif index == 1 and int(operand):
                        # append second operand to operand_set2 list
                        operand_set2.append(operand)

                except ValueError:
                    # return error message
                    return 'Error: Numbers must only contain digits.'
                
            # if-else statement to determine if currently-iterated problem's symbol is valid
            if match.group(2) in ['+', '-']:
                # append symbol to symbol_set list
                symbol_set.append(match.group(2))

                # append answer to answer_set list
                # note: this append uses a ternary operator to determine which math operation to do based on currently-iterated symbol
                answer_set.append(str(int(operands[0]) + int(operands[1])) if match.group(2) == '+' else str(int(operands[0]) - int(operands[1])))
            
            else:
                # return error message
                return "Error: Operator must be '+' or '-'."
            
    # initialize string variables to store lines of operands, symbols, dashes, and answers
    problem_line1 = ''
    problem_line2 = ''
    problem_line3 = ''
    problem_line4 = ''

    # for-loop to loop through contents of symbol_set list
    for index, _ in enumerate(symbol_set):
        # if-elif statement to determine which of the two operands is longer, and whether the current index is last one
        if len(operand_set1[index]) > len(operand_set2[index]) and index != len(symbol_set) - 1:
            # save length of longest operator in a variable
            longest = len(operand_set1[index])

            # calculate the number of spaces to add before the second operand
            spaces = ' ' * (len(operand_set1[index]) - len(operand_set2[index]))

            # concatenate the operands, symbols, and dashes to their respective variables
            # note: each line's contents is formatted in their correct placements first prior to concatenation
            problem_line1 += f'  {operand_set1[index]}    '
            problem_line2 += f'{symbol_set[index]} {spaces}{operand_set2[index]}    '
            problem_line3 += '-' * (2 + len(operand_set1[index])) + '    '

        elif len(operand_set1[index]) > len(operand_set2[index]) and index == len(symbol_set) - 1:
            # save length of longest operator in a variable
            longest = len(operand_set1[index])

            # calculate the number of spaces to add before the second operand
            spaces = ' ' * (len(operand_set1[index]) - len(operand_set2[index]))

            # concatenate the operands, symbols, and dashes to their respective variables
            # note: each line's contents is formatted in their correct placements first prior to concatenation
            problem_line1 += f'  {operand_set1[index]}'
            problem_line2 += f'{symbol_set[index]} {spaces}{operand_set2[index]}'
            problem_line3 += '-' * (2 + len(operand_set1[index]))

        elif len(operand_set1[index]) < len(operand_set2[index]) and index != len(symbol_set) - 1:
            # save length of longest operator in a variable
            longest = len(operand_set2[index])

            # calculate the number of spaces to add before the second operand
            spaces = ' ' * (2 + len(operand_set2[index]) - len(operand_set1[index]))

            # concatenate the operands, symbols, and dashes to their respective variables
            # note: each line's contents is formatted in their correct placements first prior to concatenation
            problem_line1 += f'{spaces}{operand_set1[index]}    '
            problem_line2 += f'{symbol_set[index]} {operand_set2[index]}    '
            problem_line3 += '-' * (2 + len(operand_set2[index])) + '    '

        elif len(operand_set1[index]) < len(operand_set2[index]) and index == len(symbol_set) - 1:
            # save length of longest operator in a variable
            longest = len(operand_set2[index])

            # calculate the number of spaces to add before the second operand
            spaces = ' ' * (2 + len(operand_set2[index]) - len(operand_set1[index]))
            problem_line1 += f'{spaces}{operand_set1[index]}'
            problem_line2 += f'{symbol_set[index]} {operand_set2[index]}'
            problem_line3 += '-' * (2 + len(operand_set2[index]))

        elif len(operand_set1[index]) == len(operand_set2[index]) and index != len(symbol_set) - 1:
            # save length of longest operator in a variable
            longest = len(operand_set1[index])

            # concatenate the operands, symbols, and dashes to their respective variables
            # note: each line's contents is formatted in their correct placements first prior to concatenation
            problem_line1 += f'  {operand_set1[index]}    '
            problem_line2 += f'{symbol_set[index]} {operand_set2[index]}    '
            problem_line3 += '-' * (2 + len(operand_set1[index])) + '    '

        elif len(operand_set1[index]) == len(operand_set2[index]) and index == len(symbol_set) - 1:
            # save length of longest operator in a variable
            longest = len(operand_set1[index])

            # concatenate the operands, symbols, and dashes to their respective variables
            # note: each line's contents is formatted in their correct placements first prior to concatenation
            problem_line1 += f'  {operand_set1[index]}'
            problem_line2 += f'{symbol_set[index]} {operand_set2[index]}'
            problem_line3 += '-' * (2 + len(operand_set1[index]))

        # if-statement to determine whether to print answers too
        if display_ans == True:
            # if-elif statement to determine if the currently-iterated answer is longer than the longest operand, and whether the current index is last one
            if len(answer_set[index]) < longest and index != len(symbol_set) - 1:
                # calculate the number of spaces to add before the answer
                spaces = ' ' * (longest - len(answer_set[index]))

                # concatenate the answer to its variable
                # note: this line's contents is formatted in their correct placements first prior to concatenation
                problem_line4 += f'{spaces}{answer_set[index]}    '

            elif len(answer_set[index]) < longest and index == len(symbol_set) - 1:
                # calculate the number of spaces to add before the answer
                spaces = ' ' * (longest - len(answer_set[index]))

                # concatenate the answer to its variable
                # note: this line's contents is formatted in their correct placements first prior to concatenation
                problem_line4 += f'{spaces}{answer_set[index]}'

            elif len(answer_set[index]) > longest and index != len(symbol_set) - 1:
                # calculate the number of spaces to add before the answer
                spaces = ' ' * (len(answer_set[index]) - longest)

                # concatenate the answer to its variable
                # note: this line's contents is formatted in their correct placements first prior to concatenation
                problem_line4 += f'{spaces}{answer_set[index]}    '

            elif len(answer_set[index]) > longest and index == len(symbol_set) - 1:
                # calculate the number of spaces to add before the answer
                spaces = ' ' * (len(answer_set[index]) - longest)

                # concatenate the answer to its variable
                # note: this line's contents is formatted in their correct placements first prior to concatenation
                problem_line4 += f'{spaces}{answer_set[index]}'

            elif len(answer_set[index]) == longest and index != len(symbol_set) - 1:
                # concatenate the answer to its variable
                # note: this line's contents is formatted in their correct placements first prior to concatenation
                problem_line4 += f'  {answer_set[index]}    '

            elif len(answer_set[index]) == longest and index == len(symbol_set) - 1:
                # concatenate the answer to its variable
                # note: this line's contents is formatted in their correct placements first prior to concatenation
                problem_line4 += f'  {answer_set[index]}'

    # return arranged math result
    # note: this result uses a ternary operator to determine whether to display result as well based on passed boolean value
    return f'{problem_line1}\n{problem_line2}\n{problem_line3}\n{problem_line4}' if display_ans == True else f'{problem_line1}\n{problem_line2}\n{problem_line3}'