FROM quay.io/debezium/postgres:15

COPY sql/01_create_tables.sql /docker-entrypoint-initdb.d/
COPY sql/02_mnist_train.sql /docker-entrypoint-initdb.d/