class Dog(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        print "my dog name is",self.name
    def talk(self):
        print "mung mung"
class ShihTzuDog(Dog):
    def talk(Dog):
        print "si si"        
class Maltese(Dog):
    def talk(Dog):
        print "mal mal"
def DogSound():
	mydog=Dog('poppy')
	mydog.talk()
	myshihtzu=ShihTzuDog('poppy')
	myshihtzu.talk()
	mymaltese=Maltese('poppy')
	mymaltese.talk()

def lab14(): 
    DogSound() 
     
def main():    
    lab14() 
 
if __name__=="__main__": 
    main() 
