import os
mydir=os.getcwd()
filename='python.txt'

def File_homework1():
	try:
    		myfilename=os.path.join(mydir,filename)
    		myfile=open(myfilename)
    		for line in myfile:
        		if line.find('Python')>=0:
           			 print line
    		myfile.close()
	except IOError as e:
    		print e

def File_homework2():
	myfile=open('output.txt','w')
	line1='first line\n'
	myfile.write(line1)
	line2='second line\n'
	myfile.write(line2)
	line3="third line"
	myfile.write(line3)
	myfile.close()
	myfile=open('output.txt','r')
	contents=myfile.readlines() 
	for a in range(0,len(contents)): 
    		if contents[a].find('l') >= 0: 
        		result = contents[a].split() 
    		for b in range(0,len(result)): 
        		if result[b].find('l') >= 0: 
            			print result[b].upper() 
	myfile.close() 

def lab12():
	File_homework1()
	File_homework2()

def main():
	lab12()

if __name__=="__main__": 
     main() 
