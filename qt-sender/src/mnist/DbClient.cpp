#include "include/mnist/DbClient.h"
#include <iostream>
#include <QByteArray>

const QString DbClient::USER_NAME = "postgres";
const QString DbClient::PASSWORD = "postgres";
const QString DbClient::DB_NAME = "postgres";
const QString DbClient::DEFAULT_DB_HOSTNAME = "127.0.0.1";
const QString DbClient::DEFAULT_TABLE_NAME = "mnist_test";


DbClient::DbClient() {
    init(DEFAULT_DB_HOSTNAME, DEFAULT_TABLE_NAME);
}

DbClient::DbClient(QString dbHostname, QString tableName) {
    init(dbHostname, tableName);
}

DbClient::~DbClient() {
    db.close();
    QSqlDatabase::removeDatabase("mnist");
}

void DbClient::init(QString dbHostname, QString tableName) {
    db = QSqlDatabase::addDatabase("QPSQL", "mnist");
    db.setHostName(dbHostname);
    db.setDatabaseName(DB_NAME);
    db.setUserName(USER_NAME);
    db.setPassword(PASSWORD);
    bool ok = db.open();
    if (ok) {
        std::cout << "Connected to the database" << std::endl;
    }
    else {
        std::cout << "Failed to connect to the database" << std::endl;
    }
}

void DbClient::put(QString key, QByteArray value) {
    QSqlQuery query(db);
    query.prepare("INSERT INTO mnist_test (id, label, pixels) VALUES (:id, :label, :pixels)");
    query.bindValue(":id", key);
    query.bindValue(":label", 0);
    query.bindValue(":pixels", value);
    query.exec();
    std::cout << "Sent data to the DB" << std::endl;
}
