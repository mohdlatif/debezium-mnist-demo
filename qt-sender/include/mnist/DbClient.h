#ifndef DBCLIENT_H
#define DBCLIENT_H

#include <QtSql>
#include <QSqlDatabase>

/**
 * @brief The DB client for sending the data into Postgres DB.
 */
class DbClient : public QObject {
    Q_OBJECT

public:
    DbClient();
    DbClient(QString dbHostname, QString tableName);
    ~DbClient();

    void put(QString key, QByteArray value);

private:
    static const QString USER_NAME;
    static const QString PASSWORD;
    static const QString DB_NAME;
    static const QString DEFAULT_DB_HOSTNAME;
    static const QString DEFAULT_TABLE_NAME;

    QSqlDatabase db;
    QString dbHostname;
    QString tableName;
    QByteArray imageContent;

    void init(QString dbHostname, QString tableName);
};


#endif // DBCLIENT_H
