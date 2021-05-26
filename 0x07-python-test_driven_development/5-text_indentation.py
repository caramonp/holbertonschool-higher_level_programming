#!/usr/bin/python3
""" text_indentation returns 2 newlines after each ['.', '?', ':']:
"""


def text_indentation(text):
    """ 
    prints "text" with 2 newlines after each of these char: ['.', '?', ':']
    checks if "text" is a str
    first loop removes spaces after each special chars
    second loop adds 2 newlines after each special chars
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    char_special = ['.', '?', ':']

    index = 0
    for i in text:
        if i in char_special:
            if text[index + 1] == " ":
                text = text[:index + 1] + text[index + 2:]
        else:
            index += 1

    index = 0
    for i in text:
        if i in char_special:
            text = text[:index + 1] + '\n\n' + text[index + 1:]
            index += 3
        else:
            index += 1

    print(text, end='')
