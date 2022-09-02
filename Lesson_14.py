count = -1

for x in range (0,7):
    if x == 3 or x == 5:
        continue #goes back to the top of the loop
    print x,#comma prints it all on the same line
print
while count <=7:
    count+=1
    if count == 3 or count == 5:
        continue
    print count,