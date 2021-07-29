class Persona:
    def__new__(): 
        print("new")
        return super(Persona,cls).__new__(cls)
    def__int__(self):
        print("init")
p=Persona()
