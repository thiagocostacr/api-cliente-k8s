import Cliente

INSERE_CLIENTES='INSERT INTO clientes.cliente(nome, email, cpf, dtnascimento, estado) VALUES(%s, %s, %s, %s, %s)'
LISTAR_CLIENTES='SELECT * FROM clientes.cliente WHERE estado=true'
LISTAR_ESPECIFICO='SELECT * FROM clientes.cliente WHERE id = %s and estado=true'
EXCLUIR_CLIENTE='UPDATE cliente SET estado=false WHERE id=%s'
ATUALIZAR_CLIENTE='UPDATE cliente SET nome=%s, email=%s, cpf=%s, dtNascimento=%s WHERE id=%s'

class ClienteDAO:
    def __init__(self, db):
        self.__db = db

    def inserir(self, cliente):
        cursor = self.__db.connection.cursor()
        cursor.execute(INSERE_CLIENTES, (cliente.nome, cliente.email, cliente.cpf, cliente.dtNascimento, True))
        self.__db.connection.commit()
        return cliente

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(LISTAR_CLIENTES)
        cliente = cursor.fetchall()
        return cliente

    def listarId(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(LISTAR_ESPECIFICO, (id,))
        cliente = cursor.fetchone()
        return cliente

    def excluir(self, id):
        try:
            cursor = self.__db.connection.cursor()
            cursor.execute(EXCLUIR_CLIENTE, (id,))
            self.__db.connection.commit()
            return id
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            return None

    def atualizar(self, id, cliente):
        cursor = self.__db.connection.cursor()
        cursor.execute(ATUALIZAR_CLIENTE, (cliente.nome, cliente.email, cliente.cpf, cliente.dtNascimento, id))
        self.__db.connection.commit()
        return cliente
