def reverseList(myList):
    # These variables will keep track of indices in our list
    pos1 = 0
    pos2 = len(myList)-1
    # In each loop, we will swap the val at pos1 with the val at pos2, meaning we only need to loop half of the length of the list
    numOfLoops = int(pos2/2)+1
    newList = myList
    
    while pos1 < numOfLoops:
        # I made this variable to hold the value of myList[pos1] because I needed it but it was getting overwritten
        secondVal = myList[pos1]
        newList[pos1] = myList[pos2]
        newList[pos2] = secondVal
        # Adjust the pos variables accordingly
        pos1 += 1
        pos2 -= 1
    return newList

someList = [43,-5,5,1,0,23,9]
print(reverseList(someList))