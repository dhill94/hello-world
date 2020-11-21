def isSorted(lyst):
    if len(lyst) >= 0 and len(lyst) < 2:
        return True
    for x in range(len(lyst) - 1):
        if lyst[x] > lyst[x + 1]:
            return False
    return True
