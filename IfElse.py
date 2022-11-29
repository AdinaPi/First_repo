# print('ma duc la mare')
# va_fi_frumos = False
# if va_fi_frumos == True :
#     print('ma voi distra')
#     print('ma voi bronza')
# print('nu ma duc la mare')

nr = -6

# ora = int(input("introdu ora"))
# if ora < 0:
#     print('ora negativa')
# elif ora < 12:
#     print('Buna dimineata')
# elif ora < 18:
#     print('Buna ziua')
# elif ora < 21:
#     print('Buna seara')
# elif ora < 24:
#     print('Noapte buna')
# else:
#     print('Error')

varsta = int(input("introdu varsta"))
if varsta < 1:
    print('varsta invalida')
elif varsta < 18:
    print('nu poate paria')
elif varsta >= 18:
    print('poate paria')
else:
    print('error')