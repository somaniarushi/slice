
import re

#TODO: Convert to arguments accepted from the terminal later.
lst = [1, 2, 3, 4]
slice = "[:2:-1]"

ptn = r"^\[(-?\d*):(-?\d*):?(-?\d*)\]$"

class NoneObject:
    """
    Unique object with no particular properties.
    """
    def __repr__(self):
        return "none"

class Yielder:
    """
    A class that returns the next value on a call to next.
    """
    none = NoneObject()
    def __init__(self, lst, start, end, step):
        self.lst = lst
        self.start = int(start) if is_digit(start) else self.none
        self.end = int(end) if is_digit(end) else self.none
        self.step = int(step) if is_digit(step) else 1

    def next(self):
        if self.start is self.none:
            if self.step < 0:
                self.start = len(lst)-1
            else:
                self.start = 0
            return None
        else:
            if (self.start < 0 or self.start == len(lst) or (self.end is not self.none and self.start == self.end)):
                return None
            val = self.lst[self.start]
            self.start += self.step
            return val

def is_digit(i):
    """
    Return true if the string i is a digit.
    """
    if i.startswith("-"):
        return i[1:].isdigit()
    else:
        return i.isdigit()

def slicer(lst, slice):
    """
    Returns the list `lst` slices according to the string `slice`.
    """
    matched = re.findall(ptn, slice)
    if (not matched or len(matched) > 1):
        raise SyntaxError("Slice string input syntax incorrect")
    start, end, step = matched[0]

    end_blank = not is_digit(end)
    start_blank = not is_digit(start)

    y = Yielder(lst, start, end, step)

    result = []
    first_none = True

    # End is exclusive.
    while (True):
        val = y.next()
        if not val:
            if first_none:
                first_none = False
                continue
            else:
                if (not (start_blank or end_blank)):
                    return []
                return result
        else:
            result.append(val)
    return result


if __name__ == "__main__":
    res = slicer(lst, slice)
