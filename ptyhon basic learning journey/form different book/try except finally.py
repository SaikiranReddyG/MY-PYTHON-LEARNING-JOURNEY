class voters_eligibility(Exception) :
    def __int__(self):
        super()

try :
    age = 99
    print('age is ' + str(age))
    if age < 18 :
      raise voters_eligibility
except voters_eligibility :
    print('age is less than 18')
except TypeError :
    print('age is not numeric')
else :
    print('age is greater or equal to 18')
finally :
    print('end of program')
