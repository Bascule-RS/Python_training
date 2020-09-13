class PS:
    def __init__(self, pseudo, degre, age):
        self.pseudo=pseudo
        self.degre=degre
        self.age=age
        
    def complet(self):
        return '1:{}\t 2:{}\t 3:{}'.format(self.pseudo,self.degre,self.age)
        
PS_1 = PS('shooting_star','6,5','34')
PS_2 = PS('swang','4,5','32')
PS_3 = PS('Mâra','6','38')
print('Bienvenue sur le programme de fichage des PS:\n')
print('1: Pseudo\t 2: Niveau de PS\t 3: age')

print(PS_1.complet())
print(PS_2.complet())