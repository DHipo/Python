#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <ctime>
#include <cstdio>
#include <cstdlib>

using namespace std;

bool CheckINT(string);

class Cliente{
    public: 
        Cliente(string name, string subname, string pass, int pin,int ID, float Balance){
            this->NomApe = name+" "+subname;
            this->id = ID;
            this->balance = Balance;
            this->password = pass;
            this->pin = pin;
        };
        Cliente(void){};
        string NomApe, password;
        int id, pin, balance;
};

class Bank {
    public: 
        Cliente * CurrentClient;
        bool HasCurrentClient = false;
        void deposit(int amount);
        void withdraw(int amount);
        void transfer(int amount, Cliente &client2);
        float getBalance(Cliente &cliente);
        void Show_Client(Cliente &cliente);
        void Show_Client_List(void);
        int Get_Clients(void);
        int POP(string name, string subname, string pass, int pin,int id, float balance);
        int Get_Client_By_Name(string name);
        void Remove_Client(Cliente &client);
        void refresh(void);
};

Bank Banco;
vector<Cliente> ArrCliente;

void PrintJson(void);
void AddClient(Cliente &, fstream &, bool);

int Bank::Get_Clients(void){
    ifstream PF("UsersRegisters.txt");
    PF.seekg(0,ios::beg);
    int index=0;
    if(PF.is_open()){
        while(!PF.eof()){
            int id, pin;
            float balance;
            string name, subname, pass;
            PF>>name>>subname>>pass>>pin>>id>>balance;
            ArrCliente.push_back(Cliente(name,subname,pass,pin,id,balance));
            index++;
        }
    }
    PF.close();
    
    return index;
}

int Bank::POP(string name, string subname, string pass, int pin,int id, float balance){
    fstream PF("UsersRegisters.txt", fstream::out | fstream::in);
    PF.seekg(0, ios::end);
    ArrCliente.push_back(Cliente(name, subname, pass,pin,id, balance));
    if(PF.is_open()){
        PF<<"\n"<<name<<" "<<subname<<" "<<pass<<" "<<pin<<" "<<id<<" "<<balance;
    }
}

int Bank::Get_Client_By_Name(string name){
    Banco.refresh();
    int index=0;
    for(int i=0; i<ArrCliente.size(); i++){
        if(ArrCliente[i].NomApe==name){
            index=i;
            break;
        }else{
            index=-1;
        }
    }
    return index;
}

void Bank::deposit(int amount){
    this->CurrentClient->balance+=amount;
    cout<<"\nEl nuevo balance del cliente es: $"<<this->CurrentClient->balance<<endl;
    cout<<"[--------------------------------------------------------------------------------]"<<endl;
    Banco.refresh();
}

void Bank::refresh(void){
    fstream PF("UsersRegisters.txt", fstream::out);
    PF.clear();
    if(PF.is_open()){
        for(int i=0; i<ArrCliente.size(); i++){
            if(i == 0)  PF<<""<<ArrCliente[i].NomApe<<" "<<ArrCliente[i].password<<" "<<ArrCliente[i].pin<<" "<<ArrCliente[i].id<<" "<<ArrCliente[i].balance;
                else PF<<"\n"<<ArrCliente[i].NomApe<<" "<<ArrCliente[i].password<<" "<<ArrCliente[i].pin<<" "<<ArrCliente[i].id<<" "<<ArrCliente[i].balance;
        }
    }
    PF.close();
}

void Bank::withdraw(int amount){
    if(amount<=this->CurrentClient->balance){
        this->CurrentClient->balance-=amount;
        cout<<"\nEl nuevo balance del cliente es: $"<<this->CurrentClient->balance<<endl;
        cout<<"[--------------------------------------------------------------------------------]"<<endl;
        Banco.refresh();
    }else{
        cout<<"\nEl cliente no tiene suficiente saldo"<<endl;
        cout<<"[--------------------------------------------------------------------------------]"<<endl;
    } 
}

void Bank::transfer(int amount, Cliente &client2){
    if(amount<=this->CurrentClient->balance){
        this->CurrentClient->balance-=amount;
        client2.balance+=amount;
        cout<<"\nTu balance actual es: $"<<this->CurrentClient->balance<<endl;
        cout<<"\nEl nuevo balance de "<<client2.NomApe<<" es: $"<<client2.balance<<endl;
        cout<<"[--------------------------------------------------------------------------------]"<<endl;
        Banco.refresh();
    }else{
        cout<<"\nEl cliente no tiene suficiente saldo"<<endl;
    } 
}

float Bank::getBalance(Cliente &cliente){
    int index = Banco.Get_Client_By_Name(cliente.NomApe);
    if(index!=-1){
        return ArrCliente[index].balance;
    }else{
        cout<<"\nEl cliente no existe"<<endl;
    }
}

void Bank::Show_Client(Cliente &cliente){
    int index = Banco.Get_Client_By_Name(cliente.NomApe);
    if(index!=-1){
        cout<<"\nNombre: "<<ArrCliente[index].NomApe<<" id: "<<ArrCliente[index].id<<" balance: $"<< ArrCliente[index].balance<<endl;
        cout<<"[--------------------------------------------------------------------------------]"<<endl;
    }else{
        cout<<"\nEl cliente no existe"<<endl;
        cout<<"[--------------------------------------------------------------------------------]"<<endl;
    }
}

void Bank::Remove_Client(Cliente &client){
    int index = Banco.Get_Client_By_Name(client.NomApe);
    if(index!=-1){
        ArrCliente.erase(ArrCliente.begin()+index);
        cout<<"\nEl cliente ha sido eliminado"<<endl;
        cout<<"[--------------------------------------------------------------------------------]"<<endl;
        Banco.refresh();
    }else{
        cout<<"\nEl cliente no existe"<<endl;
        cout<<"[--------------------------------------------------------------------------------]"<<endl;
    }
}

void Bank::Show_Client_List(void){
    int veri=1;
    cout<<"\tLista de clientes: "<<endl;
    for(int i=0; i<ArrCliente.size(); i++){
        if(Banco.HasCurrentClient == true){
            if(ArrCliente[i].NomApe == Banco.CurrentClient->NomApe){
                cout<<"\n"<<(i+1)<<". (Usted) Nombre: "<<Banco.CurrentClient->NomApe<<"| Pin:"<<Banco.CurrentClient->pin<<" | ID: "<<Banco.CurrentClient->id<<" | Balance: $"<<Banco.CurrentClient->balance<<endl;
            }else cout<<"\n"<<(i+1)<<". Nombre: "<<ArrCliente[i].NomApe<<" | ID: "<<ArrCliente[i].id<<endl;
        }else cout<<"\n"<<(i+1)<<". Nombre: "<<ArrCliente[i].NomApe<<" | ID: "<<ArrCliente[i].id<<endl;
    cout<<"[--------------------------------------------------------------------------------]"<<endl;
    }
    while(veri == 1){
        cout<<"\nDesea seguir viendo la lista de clientes? (1. Si / 2. No)"<<endl;
        cin>>veri;
    }
}

void delay(int secs) {
  for(int i = (time(NULL) + secs); time(NULL) != i; time(NULL));
}

void ClientOptions(void){
    int amount,index, veri=0, times=0;
    string name, subname, aux,opc;
    
    while (veri == 0 || opc[0] == '3'){
        system("@cls||clear");
        cout<<"Menu principal del cliente "<<Banco.CurrentClient->NomApe<<endl;
        cout<<"[--------------------------------]"<<endl;
        cout<<"1. Depositar"<<endl;
        cout<<"2. Retirar"<<endl;
        cout<<"3. Transferir"<<endl;
        cout<<"4. Recrear contraseña"<<endl;
        cout<<"5. Ver saldo"<<endl;
        cout<<"6. Ver lista de clientes"<<endl;
        cout<<"7. Volver al menu principal"<<endl;
        cout<<"8. Salir"<<endl;
        cout<<"[--------------------------------]"<<endl;
        cout<<"Seleccione una opcion: \n--->";
        cin>>opc;
        if (opc.size() > 1) {
            system("@cls||clear");
            cout<<"\nOpcion invalida"<<endl;
            delay(2);
        }else{
            switch(opc[0]){
                case '1':
                    system("@cls||clear");
                    cout<<"Ingrese el monto a depositar: \n-->";
                    cin>>amount;
                    Banco.deposit(amount);
                    cout<<"[--------------------------------]"<<endl;
                    cout<<"Deposito exitoso."<<endl;
                    delay(2);
                    break;
                case '2':
                    system("@cls||clear");
                    cout<<"Ingrese el monto a retirar: "<<endl;
                    cin>>amount;
                    Banco.withdraw(amount);
                    cout<<"Retiro exitoso."<<endl;
                    delay(2);
                    break;
                case '3':
                    system("@cls||clear");
                    cout<<"Ingrese el monto a transferir: "<<endl;
                    cin>>amount;
                    cout<<"Ingrese el nombre del cliente a transferir: "<<endl;
                    cin>>name>>subname;
                    aux = name+" "+subname;
                    index = Banco.Get_Client_By_Name(aux);
                    if(index!=-1 && amount<=Banco.CurrentClient->balance && amount>0){ 
                        Banco.transfer(amount, ArrCliente[index]);
                        cout<<"Transferencia exitosa."<<endl;
                        delay(2);
                    }else{
                        cout<<"\nEl cliente no existe o usted no posee los fundos suficientes."<<endl;
                        delay(2);
                    }
                    break;
                case '4': 
                    times = 0;
                    system("@cls||clear");
                    do{
                        cout<<"Ingrese su contraseña actual: "<<endl;
                        cin>>aux;
                        if(aux == Banco.CurrentClient->password && times < 3){
                            cout<<"Ingrese su nueva contraseña: "<<endl;
                            cin>>aux;
                            Banco.CurrentClient->password = aux;
                            Banco.refresh();
                            cout<<"Contraseña cambiada exitosamente."<<endl;
                            delay(2);
                            break;
                        }else{
                            system("@cls||clear");
                            cout<<"\nLa contraseña ingresada no es correcta.\nIntente nuevamente."<<endl;
                            delay(2);
                        }
                    }while(times < 3);
                    break;
                case '5':
                    system("@cls||clear");
                    cout<<"El saldo actual del cliente es: $"<<Banco.CurrentClient->balance<<endl;
                    delay(2);
                    break;
                case '6':
                    system("@cls||clear");
                    Banco.Show_Client_List();
                    break;
                case '7': 
                    break;
                case '8':
                    system("@cls||clear");
                    cout<<"\nGracias por utilizar nuestro servicio"<<endl;
                    veri = 1;
                    break;
            }
        }
    }
}   

void Menu(void){
    int veri=0, index, times=0,count;
    string name, subname,aux,pass,pin,balance, opc;
    while(veri == 0 || opc[0] == '5'){
        system("@cls||clear");
        cout<<"\t\tBienvenido al banco de Bautista D'Hipolito"<<endl;
        cout<<"[--------------------------------------------------------------------------------]"<<endl;
        delay(1);
        cout<<"1. Iniciar sesion"<<endl; 
        cout<<"2. Crear cuenta"<<endl;
        cout<<"3. Remover cuenta (Working in progress)"<<endl;
        cout<<"4. Ver clientes registrados"<<endl;
        cout<<"5. Salir"<<endl;
        cout<<"[--------------------------------]"<<endl;
        cout<<"Seleccione una opcion: \n--->";
        cin>>opc;
        if (opc.size() > 1) {
            system("@cls||clear");
            cout<<"\nOpcion invalida"<<endl;
            delay(2);
        }else{
            switch(opc[0]){
                case '1':
                    system("@cls||clear");
                    times = 0;
                    cout<<"Ingrese su nombre de usuario: \n--->";
                    cin>>name>>subname;
                    aux = name+" "+subname;
                    index = Banco.Get_Client_By_Name(aux);
                    if(index!=-1){
                        while(pass != ArrCliente[index].password && times<3){
                            if(times >= 1) {
                                system("@cls||clear");
                                cout<<"Ingrese su nombre de usuario: \n--->";
                                cout<<aux<<endl;
                                cout<<"Contraseña incorrecta. Intentelo de nuevo."<<endl;
                            }
                            cout<<"Ingrese su constraseña: \n--->";
                            cin>>pass;
                            if(pass == ArrCliente[index].password){
                                Banco.CurrentClient = &ArrCliente[index];
                                Banco.HasCurrentClient = true;
                                cout<<"\nBienvenido "<<Banco.CurrentClient->NomApe<<"."<<endl;
                                delay(2);veri++;
                            }else if(times == 3){
                                cout<<"\nHa superado el numero de intentos permitidos."<<endl;
                                delay(2);
                                break;
                            }
                            times++; 
                        }
                    }else {
                        cout<<"\nEl cliente no existe"<<endl;
                        delay(2);
                    }
                    break;
                case '2':
                    count = 0;
                    system("@cls||clear");
                    times = 0;
                    //Le pido el nombre y apellido
                    cout<<"Ingrese el nombre completo del cliente: "<<endl;
                    cin>>name>>subname;
                    cout<<"[--------------------------------]"<<endl;
                    do{//Le pido un pin valido
                        if(count) cout<<"El pin ingresado es invalido. Intente nuevamente."<<endl;
                        cout<<"Ingrese codigo de pin: "<<endl;
                        cin>>pin;
                    }while(!CheckINT(pin));
                    cout<<"[--------------------------------]"<<endl;
                    do{//Le pido una contraseña valida
                        if(times >= 1){
                            system("@cls||clear");
                            cout<<"Ingrese el nombre completo del cliente: "<<endl;
                            cout<<name<<" "<<subname<<endl;
                            cout<<"[--------------------------------]"<<endl;
                            cout<<"Ingrese codigo de pin: "<<endl;
                            cout<<pin<<endl;
                            cout<<"[--------------------------------]"<<endl;
                            cout<<"Las contraseñas no son iguales, intente de nuevo."<<endl;
                        }
                        cout<<"Ingrese una contrasena: "<<endl;
                        cin>>pass;
                        cout<<"Ingrese de nuevo la contrasena: "<<endl;
                        cin>>aux;
                        times++;
                    }while(pass != aux && times < 3);
                    //Le pido un saldo inicial
                    cout<<"[--------------------------------]"<<endl;
                    count =0;
                    do{
                        if (count) cout<<"El saldo ingresado es invalido. Intente nuevamente."<<endl;
                        cout<<"Ingrese el saldo inicial: "<<endl;
                        cin>>balance;
                    }while(!CheckINT(balance));
                    cout<<"[--------------------------------]"<<endl;
                    Banco.POP(name,subname, pass, atoi(pin.c_str()),(time(NULL)%10000000), atoi(balance.c_str()));
                    cout<<"\nCuenta creada exitosamente."<<endl;
                    break;
                case '3':
                    system("@cls||clear");
                    cout<<"Ingrese el nombre completo del cliente: "<<endl;
                    cin>>name>>subname;
                    aux = name+" "+subname;
                    index = Banco.Get_Client_By_Name(aux);
                    if(index!=-1){
                        Banco.Remove_Client(ArrCliente[index]);
                    }else{
                        cout<<"\nEl cliente no existe"<<endl;
                    }
                    break;
                case '4':
                    system("@cls||clear");
                    Banco.Show_Client_List();
                    break;
                case '5':
                    system("@cls||clear");
                    cout<<"\nGracias por utilizar nuestro servicio"<<endl;
                    veri++;
                    break;
            }
        }
    }
    if(opc[0]!='5')ClientOptions();
}

void Initializer(void){
    Banco.Get_Clients();
}

bool CheckINT(string aux){
    int count =0;
    for(int i=0; i<aux.size(); i++)
        if(aux[i]<'0' || aux[i]>'9') count++;
    
    if (count == 0) return true;
        else return false;
}
void AddClient(Cliente & cliente, fstream & PF, bool last){
    if(last)PF<<"\t{\n\t\t\"name\": \""<<cliente.NomApe<<"\", \n\t\t\"pass\": \""<<cliente.password<<"\", \n\t\t\"id\":"<<cliente.id<<", \n\t\t\"pin\":"<<cliente.pin<<", \n\t\t\"balance\":"<<cliente.balance<<"\n\t}\n";
        else PF<<"\t{\n\t\t\"name\": \""<<cliente.NomApe<<"\", \n\t\t\"pass\": \""<<cliente.password<<"\", \n\t\t\"id\":"<<cliente.id<<", \n\t\t\"pin\":"<<cliente.pin<<", \n\t\t\"balance\":"<<cliente.balance<<"\n\t},\n";
    
}
void PrintJson(void){
    fstream PF("Cliente.json", ios::out);
    
    //Start
    PF<<"[\n";
    for(int i=0; i<ArrCliente.size(); i++){
        if((i+1) == ArrCliente.size()) AddClient(ArrCliente[i], PF, true);
            else AddClient(ArrCliente[i], PF,false);
    }
    //End
    PF<<"]";
}
