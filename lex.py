states = raw_input("dwse tis lexeis: ")
list = states.split (' ')
x = len(list)
max=list[0]
for i in range(x):
    if(len(list[i])>=len(max)):
        max=list[i]
print max
