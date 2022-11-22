from random import randint
from time import sleep
from colorama import init
from termcolor import colored
import os
import json
 
init()

class Edificio:
    def __init__(self, dps = []) -> None:
        self.deps = dps
        self.floor = []
        pass

    def DisplayDeps(self):
        for dep in self.deps:
            print(colored(f'deps: {dep.GetData()}', 'white'))
    
    def setFloor(self):
        for i in range(len(self.deps)):
            if i == 0:
                self.floor.append([self.deps[:i+4]]) # [(0,1,2,3),4,5,6,7,8,9]
            if i == 4:
                self.floor.append([self.deps[i:i+3]]) # [(0,1,2,3),(4,5,6),7,8,9]
            if i == 7:
                self.floor.append([self.deps[i:]]) # [(0,1,2,3),(4,5,6),(7,8,9)]
    
    def DisplayDataF(self):
        for f in self.floor:
            print('{\n')
            for d in f:
                print(f'\t{d.GetData()},')
            print('}')


class Departamento:
    def __init__(self, h, b, p, o, s, i) -> None:
        self.id = i
        self.owner = o
        self.habitaciones = h
        self.banos = b
        self.precio = p
        self.state = s
        pass

    def DisplayData(self):
        print(f'Owner: {self.owner.GetData()}, h: {self.habitaciones}, b: {self.banos},'+colored(f' p: ${self.precio}', 'green') + f' id: {self.id}')
        
    def GetData(self):
        return ('[' + f'Owner: {self.owner.GetData()}, h: {self.habitaciones}, b: {self.banos},'+colored(f' p: ${self.precio}', 'green') + ']')

class Owner:
    def __init__(self, n, s, d) -> None:
        self.name = n
        self.surname = s
        self.description = d

    def DisplayData(self):
        print(f'name: {self.name}, surname: {self.surname}, description: {self.description}')

    def GetData(self):
        return ('[' + f'name: {self.name}, surname: {self.surname}, description: {self.description}'+']')

namesOwner = ['Tiziano', 'Lucio', 'Ramiro', 'Santiago', 'FERNANFLOO', 'Magali', 'Bautista', 'Marcelo', 'Pedro', 'El negro',
                    'San Martin', 'Israel','Piñon Fijo', 'Roberto', 'Marta', 'Mirta', 'Roberta', 'Mirko', 'Anastacio', 'Penelope']
surnamesOwner = ['Louyer', 'Capezzuto', 'Carnicer', 'Romero', 'YT', 'Aldana', 'Dhipolito', 'Tineli', 'Alfonso', 'Villero',
                    'Twitter', 'Pelo', 'Toyota', 'Siderca', 'Tenaris', 'Pavelek', 'Minecraft']
DescriptionOwner = ['Fachero', 'Ludico', 'Buena Onda', 'Tiene pecas', 'Huele mal', 'Su cabeza se parece a la de Saitama', 
                    'Es negro', 'Es feo', 'Es mejor pasarlo por arriba que por el costado', 'Es rubio', 'Su mama fue mi amante',
                    'Que buena que esta su vieja', 'Tendra hermanas?', 'canta como su hermana a la noche', 
                    'Parece un jugador de futbol frustrado', 'Esos ojazos azules que tiene UwU', 'Ay que linda que esta',
                    'Es un re turro', 'Me va a chorear', 'Es re linda', 'Es carismatica', 'Se parece a la Joaqui', 
                    'Esa si es la turrita la egresada', 'Es puto', 'Su actividad favorita debe ser hacer tuerking']
stateDeps = ['on_sale', 'sold']

player = {
    'name': '',
    'surname': '',
    'options': {
        1: '',
        2: ''
    },
    'bankAccount': {},
    'description': '',
    'state':'out',
    'loginState': '',
    'floor': 0
}

AllCommands = {
    'outside': [
        '-get deps on sale', 
        '-get data owners', 
        '-get data deps', 
        '-get data edi',
        'agarrar el celular',
        'entrar',
        'irse (salir del programa)'
        ],
    'inside':[
        'salir',
        'obtener los detalles',
        'Ir hablar con un vendedor'
    ],
    'phone':[
        'guardar el celular',
        'login bank'
    ]
}

Owners = []
Deps = []
Edi = 0
dbClients = 0

def ReadJson(ruta):
    with open(ruta, "r") as contenido:
        return json.load(contenido)

def init():
    global Edi, dbClients
    dbClients = ReadJson(os.path.relpath('LE-Ejercicio/Banco/Cliente.json'))
    print('\n\n\t\t\tLoading...\n\n\n')
    for i in range(10):
        Owners.insert(i,Owner(
            namesOwner[randint(0,len(namesOwner)-1)],
            surnamesOwner[randint(0, len(surnamesOwner)-1)],
            DescriptionOwner[randint(0, len(DescriptionOwner)-1)]))
        Deps.insert(i,Departamento(randint(1,4),
            randint(1,3),
            randint(1200000,5000000), 
            Owners[randint(0, len(Owners)-1)], 
            stateDeps[randint(0,len(stateDeps)-1)], i))
        sleep(0.520)
        
    for i in Deps:
        Edi = Edificio(Deps)
        Edi.setFloor()

def Inside():
    player['state'] = 'inside'
    os.system('cls')
    if player['floor'] == 0:
        print('Entraste al edificio. Logras ver 4 departamentos \n')
    player['options'][2] = input('Que deseas hacer?\n--->')
    while player['options'][2] != 'salir':
        match player['options'][2]:
            case 'obtener los detalles':
                for dep in Edi.floor[player['floor']]:
                    for d in dep:
                        if d.state == 'on_sale':
                            d.DisplayData()
                        else:
                            print(f'El departamento {d.id}, no esta a la venta.')
            case 'salir':
                print('okey, sales del edificio')
            case 'Ir hablar con un vendedor':
                player['state'] = 'talking'
                for f in Edi.floor:
                    for d in f:
                        if d.state == 'on_sale':
                            print(f'El departamento {d.id} esta a la venta, su dueño se llama {d.owner.name}')
                player['options'][3] = input('A cual vendedor quiere dirigirse?')
                #for i in Edi.floor:
                #    if player['options'][3] == Deps[i].id or player['options'][3] == Deps[i].owner.name:
                #        Talking()
            case 'help':
                GetCommands()

        player['options'][2] = input('Que desea hacer?\n--->')
    player['state'] = 'out'

def Login():
    os.system('cls')
    print('\t\tLogin\n\n')
    
    #Getting the name user
    while player['loginState'] != 'landed_username':
        
        if player['loginState'] == 'invalid_username':
            inpt = input('El nombre ingresado no esta registrado. \nIngrese un nombre usuario registrado en el banco:\n--->')
        else:
            inpt = input('Ingrese su nombre usuario en el banco:\n--->')
        
        
        if inpt == 'exit':
            return 
        
        for clients in dbClients:
            if clients['name'] == inpt:
                player['loginState'] = 'landed_username'
                player['bankAccount'] = clients.copy()
                print(player['bankAccount'])
                print('succes!')

        if player['loginState'] != 'landed_username':
            player['loginState'] = 'invalid_username'
    
    #Getting the pássword
    while player['loginState'] != 'landed_password':
        
        if player['loginState'] == 'invalid_password':
            inpt = input('La contraseña ha sido incorrecta. \nIngrese la contraseña registrada en el banco:\n--->')
        else:
            inpt = input('Ingrese su contraseña:\n--->')
        
        if inpt == '-return username':
            break
        
        if inpt == 'exit':
            return 
        
        if player['bankAccount']['pass'] == inpt:
            player['loginState'] = 'landed_password'
            print('succes!')
        else:
            player['loginState'] = 'invalid_password'
    
    os.system('cls')

def Register():
    path = os.path.relpath('LE-Ejercicio/Banco/Main.exe')
    os.system(f'start {path}')

def GetCommands():
    print('commands:\n')
    match player['state']:
        case 'out':
            commands = AllCommands['outside']
        case 'inside':
            commands = AllCommands['inside']
        case 'phone':
            commands = AllCommands['phone']
    for command in commands:
        print(f'\t{commands.index(command)}.{command}')

def main():
    init()
    os.system('cls')
    print('\t\tBienvenido al Edificio de Bautista D\'Hipolito\n\n')
    player['options'][1] = input('Que desea hacer?\n-->').lower()
    while player['options'][1] != 'irse':
        match player['options'][1]:
            case 'agarrar el celular':
                print('agarraste el celular')
                while player['options'][2] != 'guardar el celular':
                    player['options'][2] = input('Que deseas hacer con el celular?\n--->').lower()
                    match player['options'][2]:
                        case 'help':
                            GetCommands()
                        case 'guardar el celular':
                            print('Guardaste el celular.')
                            sleep(0.5)
                        case 'login':
                            Login()
                        case 'register':
                            Register()
            case '-get data player':
                print(player)
            case '-get deps on sale':
                for dep in Deps:
                    if dep.state == 'on_sale':
                        print(f'id: {dep.id}.')
                        dep.DisplayData()
                        print('--------------')
                awns = input('Desea comprar alguno de estos departamentos?\n--->')
                if awns == 'Si' or awns == 'si':
                    awns = input('Cual desea comparar?\n--->')
                else:
                    print('Okey, volviendo al menu principal.')
            case '-get data owners':
                for owner in Owners:
                    owner.DisplayData()
            case '-get data deps':
                for dep in Deps:
                    dep.DisplayData()
            case '-get floor':
                Edi.DisplayDataF()
            case '-get data edi':
                Edi.DisplayDeps()
            case 'entrar':
                Inside()
            case '-help':
                GetCommands()

        player['options'][1] = input('Que desea hacer?\n-->')

main()