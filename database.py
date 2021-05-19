import MySQLdb

conn = MySQLdb.connect(user='root', passwd='inmetrics', host='127.0.0.1', port=3306)

#conn.cursor().execute('DROP DATABASES `cliente`;')
#conn.commit()

criar_tabela='''SET NAMES utf8;
    CREATE DATABASE `clientes`/*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `clientes`;
    CREATE TABLE `cliente` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `nome` varchar(50) COLLATE utf8_bin NOT NULL,
        `email` varchar(100) COLLATE utf8_bin NOT NULL,
        `cpf` varchar(11) COLLATE utf8_bin NOT NULL,
        `dtnascimento` date not null,
        `estado` boolean not null,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(criar_tabela)
##conn.commit()
#cursor.close()
