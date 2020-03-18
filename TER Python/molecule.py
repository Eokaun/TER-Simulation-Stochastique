class Molecule(object):
    def __init__(self, name, taille, vitesse, init):
        self.name=name
        self.taille=taille
        self.vitesse=vitesse
        self.init=init
    
    def setTaille(self, t):
        self.taille=t
    
    def setVitesse(self, v):
        self.vitesse=v

    def setInit(self, i):
        self.init=i 
    
    
    