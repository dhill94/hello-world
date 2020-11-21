def printAll(seq):
    if seq:
        print(seq[0])
        printAll(seq[1:])
        
"""Testing to see if Lees discovery works"""
printAll("Testing Lee") #Testing String
printAll((1,5,10,20))   #Testing Tuple
printAll([1,5,10,20])   #Testing List
