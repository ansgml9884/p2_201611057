def Marks():
        
    marks=list()

    marks=[["English",100],
          ["Math",200],
          ["English",200],
          ["Math",200],
          ["English",100],
          ["Math",300]]

    Eng=0
    Eng_sum=0
    Math=0
    Math_sum=0

    for i in marks:
        if i[0]=="English":
            Eng_sum+=i[1]
            Eng+=1

        elif i[0]=="Math":
            Math_sum+=i[1]
            Math+=1

    print "Sum of English:",Eng_sum
    print "Average of English:",Eng_sum/Eng
    print "Sum of Math:",Math_sum
    print "Average of Math:",Math_sum/Math

def lab9_11():
    Marks()

def main():
    lab9_11()

if __name__=="__main__":
    main()

input()
