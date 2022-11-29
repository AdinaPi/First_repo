a = 5
b = 9
print(a + 2 == b-2)
print(a < 6 or 10 > b)

# la munte sau la mare sau la cort si dnb
munte = False
mare = False
cort = True
dnb = False
print(munte or mare)
print(munte or dnb)
print(mare or dnb)
print(munte or mare or (cort and dnb))