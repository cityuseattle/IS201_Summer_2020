income = {'Alice': 90000,
          'Bob': 100000,
          'jeff':200000,
          'Apiwat': 999998,
          'Stark':999999}

highest = max(income, key=income.get)
print("The ritchest man on earth:", end=' ')
print(highest + 'with $'+ str(income[highest]))

