#Em caso de erro executar no terminal o comando:  pip install mysql-connector-python

import mysql.connector
from MySQLdb.constants.ER import HOSTNAME, PASSWORD_FORMAT, DATABASE_NAME
from werkzeug.sansio.utils import host_is_trusted


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="150589",
        database="cadastroTeste"

    )
