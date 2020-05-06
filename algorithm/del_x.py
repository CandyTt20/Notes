def del_backspace(s, init):
    low, high = init, init + 1
    if s == '':
        return s
    elif s[low] == '#':
        return del_backspace(s[low+1:],0)
    while high < len(s):

        if s[high] != '#':
            low, high = low + 1, high + 1
        else:
            low, high = low - 1, high + 1
            if high == len(s):
                return del_backspace(s[0:low + 1] , low+1)
            elif s[high] != '#':
                return del_backspace(s[0:low + 1] + s[high:], low)
            elif low < 0:
                return del_backspace(s[high:],0)

    if low == len(s) - 1 and high == len(s):
        return s


s = "ab##"
t="c#d#"
print(del_backspace(t, 0))
