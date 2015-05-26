# convert ['11.0', '22.0', '33.0'] to [11.0, 22.0, 33.0]
def StringList2FloatList(s):
    l = []
    for each in s:
        l.append(float(each))
    return l

# convert "11 22 33" to ['11', '22', '33']
def String2StringList(s):
    l = []
    for each in s.split(" "):
        l.append( each )
    return l

# convert "11.0 22.0 33.0" to [11.0, 22.0, 33.0]
def String2FloatList(s):
    return [float(x) for x in s.split()]