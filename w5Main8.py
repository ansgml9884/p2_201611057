def bmi():
     height=raw_input("input user height (m):")
     weight=raw_input("input user weight (kg):")
     bmi=weight/(height*height)
     print bmi
     if bmi<=18.5:
        res = 'under weight'
     elif 18.5<bmi<=23:
        res = 'normal weight'
     elif 23<bmi<=25:
        res = 'over weigh'
     elif 25<bmi<=30:
        res = 'obesity'
     elif 30<bmi<=35:
        res = 'very obese'
     else:
        res = 'extremely obese'
     return res
print bmi()

