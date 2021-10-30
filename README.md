# Slice: Implementing Python Slicing for Myself

## Format
```
lst = [1, 2, 3, 4] # some list
slice = "[start:stop:step]" # a string representing the slice we wish to return
```
`start` is optional, `stop`, is optional, and the entirety of `:step` is optional.

## Pseudo-Code
1. Calculate the values of `start`, `stop` and `end`.
    1. If `start` is a number, it is set to the number + 1
    2. If `end` is a number, it is set to the number + 1
    3. If `step` is a number, it is set to itself, otherwise `1`.
2. We set `start_blank` and `stop_blank` variables to True/False based on whether the input to start and stop was blank or not.
3. We create a temp list with a `NoneObject` padding on both sides.
4.