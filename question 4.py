nembar_a = int(input("הזן מספר 1 מתוך 4 "))
nembar_b = int(input("הזן מספר 2 מתוך 4 "))
nembar_c = int(input("הזן מספר 3 מתוך 4 "))
nembar_d = int(input("הזן מספר 4 מתוך 4 "))
sum = nembar_a + nembar_d + nembar_c + nembar_c
print("זוגי וחיובי?", sum % 2 == 0 and not nembar_a > 0)
