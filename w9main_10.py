def Coffee():

    allData=list()

    allData=[["Coffee","Water","Milk","Icecream"],
    ["Espresso","No","No","No"],
    ["Long Black","Yes","No","No"],
    ["Flat White","No","Yes","No"],
    ["Cappuccino","No","Yes - Frothy","No"],
    ["Affogato","No","No","Yes"]]

    Data=allData[1:]

    milk=0
    nomilk=0

    for i in Data:
        if i[2]=="No":
            nomilk=nomilk+1
        else:
            milk=milk+1

    print "milk :",float(milk)/len(Data)*100,"%"," nomilk :",float(nomilk)/len(Data)*100,"%"

def lab9_10():
    Coffee()
     
def main():
    lab9_10()

if __name__=="__main__": 
    main()  

input()
