def rev(l):
    for i in l:
        if type(i) == str:
            l.append(rev_int(i))
        elif type(i) == str:
            l.append(rev_str(i))


def rev_int(i):
    reverse = 0
    while i > 0:
        remainder = i % 10
        reverse = (reverse * 10) + remainder
        i = i // 10
    print(reverse)


def rev_str(i):
    return i[::-1]
/

l = [23, 'hello']
rev(l)

