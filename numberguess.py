# This was written by 3y3l3ss0ur0b0r0s on 03/18/2022.
    # GitHub: https://github.com/3y3l3ss0ur0b0r0s

import random

def binary_search(l,target,low=None,high=None):

    if low is None:
        low=0
    if high is None:
        high=len(l-1)

    if high<=low:
        # high would only ever be less than low if the target was not found
        return -1

    midpoint=(low+high)//2
        # low+high refers to the length of the range we're searching
        # Double dash asks how many times 2 goes into length

    if l[midpoint]==target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target,low,midpoint-1) # Recursing here (going to call this method again)
    else:
        # target > l[midpoint]
        return binary_search(l,target,midpoint+1,high)

if __name__=='__main__':

    stopProgram=False
    validInput=False

    while stopProgram==False:

        while validInput!=True:
            length=int(input("\nHow many random numbers do you want? "))
            if length>=2:
                validInput=True
            else:
                print("\nYou need at least 2 numbers.")

        myList = set()

        while len(myList) < length:
            myList.add(random.randint(-2*length,2*length))

        myList=sorted(list(myList))

        target=int(input("\nWhat number are you looking for? "))

        targetIndex=binary_search(myList,target,0,len(myList))
        if targetIndex==-1:
            print("\nIt wasn't in the list.")
        else:
            print("\nThis is our search result: ",targetIndex)

        print("\nThis was the list: ",myList)

        validInput=False

        isDone=input("\nEnter \"X\" to end Number Guess (enter anything else to continue): ")
        if isDone=="X" or isDone=="x":
            stopProgram=True
        else:
            print("\nLet's go again then.")
