def myfile_1():
    import time
    myfile=open('output.txt','w') 
    line1='first line\n' 
    myfile.write(line1) 
    line2='second line\n' 
    myfile.write(line2) 
    line3="third" 
    myfile.write(line3) 
    myfile.close()

    fin=open('output.txt','r')
    fout=open('outputUpper.txt','w')
    for line in fin:
        words=line.split()
        if line.find('line')>=0:
            msg='[kmh edited {0}]'.format(time.strftime('%Y-%m-%d %H:%M:%S'))
            fout.write(msg)
        for word in words:
            if word=='line':
                word=word.upper()
            fout.write(word)
            fout.write(" ")
        fout.write('\n')
    fin.close()
    fout.close()
    
def myfile_2():
    data=[1,2,3,4,5,6,7,8,9,10]
    fout=open('outputNumber.txt','w')
    for i in data:
        str='{0}\t'.format(i)
        fout.write(str)
        if not i%2:
            fout.write('\n')
    fout.close()

def lab12_2():
    myfile_1()
    myfile_2()

def main():
    lab12_2()

if __name__=="__main__":
    main() 

