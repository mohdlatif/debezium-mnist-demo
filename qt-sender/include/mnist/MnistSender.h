#ifndef MNISTSENDER_H
#define MNISTSENDER_H

#include <QtCore>

#include "MnistReader.h"
#include "DbClient.h"

/**
 * @brief Convenient class which holds references to MnistReader and RestClient for easy access.
 */
class MnistSender : public QObject {
    Q_OBJECT

public:
    MnistSender();
    MnistSender(MnistReader* reader, DbClient* client);
    ~MnistSender();

    Q_INVOKABLE void sendImage(QString key);

private:
    MnistReader* reader;
    DbClient* client;

    void init(MnistReader* reader, DbClient* client);
};

#endif // MNISTSENDER_H
