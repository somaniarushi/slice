
import re

#TODO: Convert to arguments accepted from the terminal later.
lst = [1, 2, 3, 4]
slice = "[0:2:-1]"

ptn = r"^\[(-?\d*):(-?\d*):?(-?\d*)\]$"

class NoneObject:
    """
    Unique object with no particular properties.
    """
    def __repr__(self):
        return "none"

def is_digit(i):
    """
    Return true if the string i is a digit.
    """
    if i.startswith("-"):
        return i[1:].isdigit()
    else:
        return i.isdigit()

def slicer():
    """
    Returns the list `lst` slices according to the string `slice`.
    """
    matched = re.findall(ptn, slice)
    if (not matched or len(matched) > 1):
        raise SyntaxError("Slice string input syntax incorrect")
    start, end, step = matched[0]

    none = NoneObject()
    templst = [none] + lst + [none]

    start_blank = is_digit(start)
    end_blank = is_digit(end)

    start = int(start)+1 if is_digit(start) else 1
    end = int(end)+1 if is_digit(end) else len(templst)-2
    step = int(step) if is_digit(step) else 1



    result = []

    # End is exclusive.
    while (start != end):
        if (start is none):
            break
        result.append(templst[start])
        start += step

    return result


if __name__ == "__main__":
    res = slicer()
    print(f"Result is {res}")
