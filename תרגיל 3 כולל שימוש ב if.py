nembar_a = int(input("הזמן מספר 1 מתוך 5 "))
nembar_b = int(input("הזן מספר 2 מתוך 5 "))
nembar_c = int(input("הזן מספר 3 מתוך 5 "))
nembar_d = int(input("הזן מספר 4 מתוך 5 "))
nembar_e = int(input("הזן מספר 5 מתוך 5 "))
if nembar_a % 2 == 0:
    print("זוגי")
else:
    print("אי זוגי")
if nembar_b % 2 == 0:
    print("זוגי")
else:
    print("אי זוגי")
if nembar_c % 2 == 0:
    print("זוגי")
else:
    print("אי זוגי")
if nembar_d % 2 == 0:
    print("זוגי")
else:
    print("אי זוגי")
if nembar_e % 2 == 0:
    print("זוגי")
else:
    print("אי זוגי")
sum = nembar_a + nembar_b + nembar_c + nembar_d + nembar_e
avarge = (sum/5)
sum = str(sum)
avarge = str(avarge)
print("סכום", sum)
print("ממוצע", avarge)
