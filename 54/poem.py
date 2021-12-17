from textwrap import *

INDENTS = 4


def print_hanging_indents(poem):
    dedent_text = dedent(poem)

    for item in dedent_text.split("\n"):
        if item == "":
            ind = ""
        else:
            item = ind + item
            print(item)
            ind = INDENTS * " "
