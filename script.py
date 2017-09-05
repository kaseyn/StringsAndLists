words = "It's thanksgiving day. It's my birthday,too!"

words.find("day")
words = words.replace("day","month",1)
print words

# -------------------------------------------------------------------

x = [2,54,-2,7,12,98]

print min(x),max(x)

# -------------------------------------------------------------------

x = ["hello",2,54,-2,7,12,98,"world"]

newList = [x[0],x[-1]]
print newList

# -------------------------------------------------------------------

x = [19,2,54,-2,7,12,98,32,10,-3,6]

x.sort()
newList = x[0:len(x)/2]
del x[0:len(x)/2]
x.insert(0,newList)
print x