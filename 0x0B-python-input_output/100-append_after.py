#!/usr/bin/python3

""" define a append_after function """


def append_after(filename="", search_string="", new_string=""):
    """ my function """

    s = ""
    with open(filename) as file:
        for lin in file:
            s += lin

            if search_string in lin:
                s += new_string

    with open(filename, "w") as f:
        f.write(s)
