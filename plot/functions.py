# convert ['11', '22', '33'] to [11, 22, 33]
def String2Integer(s):
    l = []
    for each in s:
        l.append(int(each))
    return l