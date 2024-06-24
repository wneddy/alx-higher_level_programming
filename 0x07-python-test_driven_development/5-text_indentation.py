#!/usr/bin/python3
"""module to print text indentation"""


def text_indentation(text):
    """function to work on that"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    punct = ['.', '?', ':']
    output = []
    line = []

    for char in text:
        line.append(char)
        if char in punct:
            output.append(''.join(line).strip())
            output.append('')
            line = []
    if line:
        output.append(''.join(line).strip())
    for line in output:
        print(line)
