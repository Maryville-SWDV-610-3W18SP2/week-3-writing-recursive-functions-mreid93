def getExtremes(myList):
    # Lists have built in method which sorts them in ascending order
    myList.sort()
    # This finds our final index, which will be our max term after sorting
    maxIndex = len(myList)-1
    min = myList[0]
    max = myList[maxIndex]
    return min,max

someList = [4,-2,0,9,12,3]
print(getExtremes(someList))