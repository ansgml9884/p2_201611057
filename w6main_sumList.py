x=list()
def sumList(alist):
    for i in range(0,1000):
        if(i%4==0 and i%5!=0):
            x.append(i)
    sum=0
    for e in range(0,len(x)):
        sum=sum+x[e]

def sumList(alist):
    for i in range(0,1000):
        if(i%4==0 and i%5!=0):
             x.append(i)
    sum=0
    for e in range(0,len(x)):
        sum=sum+x[e]
    return sum

def lab6():
    alist=x
    labsum=sumList(alist)
    print labsum

def main():
    lab6()

if __name__=="__main__":
    main()

wn = raw_input("Press Enter")
