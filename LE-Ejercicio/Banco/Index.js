const data = require('./Cliente.json');
const sql = require('sqlite3').verbose();

const dataBase = new sql.Database('./Data/DataBase.db');

function InsertDataBase(){
    const lineSql = "CREATE TABLE IF NOT EXISTS Cliente (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, pass TEXT, pin INTEGER, balance INTEGER)";
    dataBase.run(lineSql, function(err) {
        if (err) console.log(err);

        console.log("Table created");
    });
}

function InsertClients() {
    const lineSql = "INSERT INTO Cliente (name, pass, pin, balance) VALUES (?, ?, ?, ?)";
    for(Cliente of data)
        dataBase.run(lineSql, [Cliente.name, Cliente.pass, Cliente.pin, Cliente.balance], function(err) {
            if(err) console.log(err.message());
        
            //console.log("Cliente inserted");
        });
}

function ShowDataBase(){
    const lineSql = "SELECT * FROM Cliente";
    dataBase.all(lineSql, function(err, rows) {
        if(err) console.log(err.message());

        for(row of rows) console.log(row);
    });
}

//InsertDataBase();
InsertClients();
//ShowDataBase();