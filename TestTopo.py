from random import randint

class Edificio:
    def __init__(self, dps = []) -> None:
        self.deps = dps
        pass

    def DisplayDeps(self):
        for dep in self.deps:
            print(f'deps: {dep.GetData()}')

class Departamento:
    def __init__(self, h, b, p, o) -> None:
        self.owner = o
        self.habitaciones = h
        self.banos = b
        self.precio = p
        pass

    def DisplayData(self):
        print(f'Owner: {self.owner.GetData()}, h: {self.habitaciones}, b: {self.banos}, p: ${self.precio}')
        
    def GetData(self):
        return ('[' + f'Owner: {self.owner.GetData()}, h: {self.habitaciones}, b: {self.banos}, p: ${self.precio}' + ']')

class Owner:
    def __init__(self, n, s, d) -> None:
        self.name = n
        self.surname = s
        self.description = d

    def DisplayData(self):
        print(f'name: {self.name}, surname: {self.surname}, description: {self.description}')

    def GetData(self):
        return ('[' + f'name: {self.name}, surname: {self.surname}, description: {self.description}'+']')

namesOwner = ['Tiziano', 'Lucio', 'Ramiro', 'Santiago', 'FERNANFLOO']
surnamesOwner = ['Louyer', 'Capezzuto', 'Carnicer', 'Romero', 'YT']
DescriptionOwner = ['Fachero', 'Ludico', 'Buena Onda', 'Tiene pecas', 'Huele mal', 'Su cabeza se parece a la de Saitama', 
                    'Es negro', 'Es feo', 'Es mejor pasarlo por arriba que por el costado', 'Es rubio', 'Su mama fue mi amante',
                    'Que buena que esta su vieja', 'Tendra hermanas?', 'canta como su hermana a la noche', 
                    'Parece un jugador de futbol frustrado']

Owners = []
Deps = []
Edi = 0

def init():
    global Edi
    for i in range(randint(1,10)):
        Owners.insert(i,Owner(namesOwner[randint(0,len(namesOwner)-1)], surnamesOwner[randint(0, len(surnamesOwner)-1)], DescriptionOwner[randint(0, len(DescriptionOwner)-1)]))
    
    for i in range(randint(1,10)):
        Deps.insert(i,Departamento(randint(1,4), randint(1,3), randint(120000,500000), Owners[randint(0, len(Owners)-1)]))
    
    for i in Deps:
        Edi = Edificio(Deps)

def main():
    init()
    print('Bienvenido al Edificio de Bautista D\'Hipolito\n\n')
    option = input('Que desea hacer?\n-->')
    match option:
        case 'show data owners':
            for owner in Owners:
                owner.DisplayData()
        case 'show data deps':
            for dep in Deps:
                dep.DisplayData()
        case 'show data edi':
            Edi.DisplayDeps()

main()