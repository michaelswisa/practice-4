nembar_a = int(input("הזן מספר 1 מתוך 5 "))
nembar_b = int(input("הזן מספר 2 מתוך 5 "))
nembar_c = int(input("הזן מספר 3 מתוך 5 "))
nembar_d = int(input("הזן מספר 4 מתוך 5 "))
nembar_e = int(input("הזן מספר 5 מתוך 5 "))
print("זוגי?", nembar_a % 2 == 0)
print("זוגי?", nembar_b % 2 == 0)
print("זוגי?", nembar_c % 2 == 0)
print("זוגי?", nembar_d % 2 == 0)
print("זוגי?", nembar_e % 2 == 0)
print("חיובי?", not nembar_a > 0)
print("חיובי?", not nembar_b > 0)
print("חיובי?", not nembar_c > 0)
print("חיובי?", not nembar_d > 0)
print("חיובי?", not nembar_e > 0)
sum = nembar_a + nembar_b + nembar_c + nembar_d + nembar_e
avarge = (sum/5)
print("סכום", sum)
print("ממוצע", avarge)
