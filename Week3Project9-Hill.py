"""

5400 nautical miles distance from north pole to equator
10000 kilometers distance from north pole to equator

10000/5400 = 1.8518518518518519

conversion = km/1.852

"""

km = input("Enter number of kilometers: ")

nm = float(km)/1.852
nm = round(nm, 6)

print(str(km), "kilometers equals", str(nm), "nautical miles.")

