nric = input('Enter an NRIC number: ')

# Type your code below]
valid = True 
prefixes = ('S', 'T', 'F', 'G')
if nric[0] in prefixes and nric[1:7].isdecimal and len(nric) == 9 and nric[-1].isalpha():
  pass
else:
    valid = False 
if not valid:
    print('NRIC is invalid.')
n = nric[0]
r = nric[8]
nric = nric.replace(n,'')
nric = nric.replace(r , '')
nric = list(nric)
digit_weight = [2,7,6,5,4,3,2]
total = 0
for i in range(len(nric)):
  total= total + (int(nric[i])*digit_weight[i])
nric.insert(0,n)
nric.insert(8,r)
if nric[0] in ('T', 'G'):
   new_total = total + 4
else:
    new_total = total 
check_digit = new_total % 11
ends_with1 = 'JZIHGFEDCBA'
ends_with2 = 'XWUTRQPNMLK'
check_last_letter = ''
if nric[0] in ('S','T'):
    check_last_letter = ends_with1[check_digit]
elif nric[0] in ('F','G'):
    check_last_letter = ends_with2[check_digit]
if nric[8] == check_last_letter:
        print('NRIC is valid.')
else:
        valid = False
if not valid:
    print('NRIC is invalid.')

