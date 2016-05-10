def Letitbe():
        
    lyrics=list()

    lyrics=[

        "When I find myself in times of trouble",

        'Mother Mary comes to me',

        'Speaking words of wisdom let it be',

        'And in my hour of darkness',

        'She is standing right in front of me',

        'Speaking words of wisdom let it be',

        'Let it be let it be',

        'Let it be let it be',

        

        'Whisper words of wisdom let it be',

        'And when the broken-hearted people',

        'Living in the world agree',

        'There will be an answer let it be',

        'For though they may be parted',

        'There is still a chance that they will see',

        'There will be an answer let it be',

     

        'Let it be let it be',

        'Let it be let it be',

        'Yeah there will be an answer let it be',

        'Let it be let it be',

        'Let it be let it be',

        'Whisper words of wisdom let it be',

     

        'Let it be let it be',

        'Ah let it be yeah let it be',

        'Whisper words of wisdom let it be',

     

        'And when the night is cloudy',

        'There is still a light that shines on me',

        'Shine on until tomorrow let it be',

        'I wake up to the sound of music',

        'Mother Mary comes to me',

        'Speaking words of wisdom let it be',

     

        'Let it be let it be',

        'Let it be yeah let it be',

        'Oh there will be an answer let it be',

        'Let it be let it be',

        'Let it be yeah let it be',

        'Whisper words of wisdom let it be']

     

    doc=lyrics

    d=dict()

    #for line in doc:

        #print line.split()

    for line in doc:
        for c in line.split():
            if c not in d:
                d[c]=1
            else:
                d[c]=d[c]+1
                
                
    under20=list()
    over20=list()

    for i in d:
        if d[i]>=20:
            over20.append(i+"("+str(d[i])+")")

        else:
            under20.append(i+"("+str(d[i])+")")

    print "Word that comes more than 20 times : ",over20
    print "Word that comes less than 20 times : ",under20

def lab9_12():
    Letitbe()

def main():
    lab9_12()

if __name__=="__main__":
    main()

input()
