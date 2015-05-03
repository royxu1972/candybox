# convert ['11', '22', '33'] to [11, 22, 33]
def StringList2IntegerList(s):
    l = []
    for each in s:
        l.append(int(each))
    return l

# convert "11 22 33" to ['11', '22', '33']
def String2StringList(s):
    l = []
    for each in s.split(" "):
        l.append( each )
    return l

# convert "11 22 33" to [11, 22, 33]
def String2FloatList(s):
    l = []
    for each in s.split(" "):
        l.append( float(each) )
    return l
