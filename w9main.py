def charCount():
    word='sangmyung university'
    allchars=list(word)
    d=dict()
    for c in allchars:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    import matplotlib
    import matplotlib.pyplot as plt
    plt.bar(range(len(d)),d.values(),align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()
def countDigitsLetters():
    word='20 Hongjimun 2-gil Jongno-gu Seoul Korea'
    allchars=list(word)         
    d=dict()
    d['number']=0
    d['word']=0
    for c in allchars:
        if c.isdigit():
            d['number']=d['number']+1
        else:
            d['word']=d['word']+1
    import matplotlib
    import matplotlib.pyplot as plt
    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), d.keys())
    plt.show()
myhome=set()
yourhome=set()
myhome={'TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'}
yourhome={'coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'}
def Mine():
    print myhome.difference(yourhome)
def Yours():
    print yourhome.difference(myhome)
def Both():
    print myhome.intersection(yourhome)
def All():
    print myhome.union(yourhome)
def Count():
    d=dict()
    for c in myhome:
        if c not in d:
            d[c]=1
        else:
            d[c]=1
    for c in yourhome:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    print d

def lab9_1():
    charCount()

def lab9_2():
    countDigitsLetters()
       
def lab9_3():
    Mine()
    Yours()
    Both()
    All()
    Count()
       
def main():
    lab9_1()
    lab9_2()
    lab9_3()
    
if __name__=="__main__":
    main() 
