

Entree = str(input("Bonjour veuillez taper/coller votre texte ici:"))
Separ = str(input("Veuillez entrer votre separateur ici:"))

x = Entree.split()
for i in x:
    print(i, end=Separ)
    
    
def will_be_implemented_later(): 
    pass
     
#When invoking the Python 2 command line interpreter with the -t option, it issues warnings about code that illegally mixes tabs and spaces. When using -tt these warnings become errors. These options are highly recommended!

#The bool type is a subclass of the int type and True and False are its only instances:

AVA = bytes(b'CIORAN')
AVAdecode = AVA.decode('utf8')
AVAreversed = reversed(AVAdecode)
print(AVAreversed)
type(AVAreversed)
#print("\nAVA vaut"+AVAreversed) 

