weight = input('Enter Weight: ')
typeOfWeight = input ('Kg? Type "k" or Lbs? Type "l": ')

weight = int(weight)
typeOfWeight = typeOfWeight.lower()

if typeOfWeight == 'k':
  print('weight in lbs: ' + str(round(weight / 0.45)))
elif typeOfWeight == 'l':
  print('weight in kgs: ' + str(round(weight * .45)))