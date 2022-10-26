weight = input('Enter Weight: ')
typeOfWeight = input ('Kg? Type "k" or Lbs? Type "l": ')

weight = int(weight)

if typeOfWeight == 'k':
  print(round(weight * 2.204))
elif typeOfWeight == 'l':
  print(weight // 2.204)