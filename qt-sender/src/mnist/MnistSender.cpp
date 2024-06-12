#include "include/mnist/MnistSender.h"
#include <iostream>
#include <QByteArray>

MnistSender::MnistSender() {
    init(new MnistReader(), new DbClient());
}

MnistSender::MnistSender(MnistReader* reader, DbClient* client) {
    init(reader, client);
}

MnistSender::~MnistSender() {
    delete reader;
    delete client;
}

void MnistSender::init(MnistReader* reader, DbClient* client) {
    this->reader = reader;
    this->client = client;
}

void MnistSender::sendImage(QString key) {
    client->put(key, reader->imgByteArray(key.toInt()));
}
