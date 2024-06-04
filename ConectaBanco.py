import sqlite3

class ConectaBanco:
    def __init__(self, db_name='reconhecimentoFacial.sqlite'):
        self.db_name = db_name
        self.conexao = None
        self.cursor = None

    def conectar(self):
        self.conexao = sqlite3.connect(self.db_name)
        self.cursor = self.conexao.cursor()

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()

    def criaBanco(self):
        try:
            self.conectar()
            self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ra TEXT NOT NULL,
            foto INTEGER
        )
        ''')

            self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS presencas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ra TEXT NOT NULL,
            data_hora TEXT,
            presente TEXT
        )
        ''')
            self.conexao.commit()
            print("Banco de dados criado com sucesso.")
        except sqlite3.Error as erro:
            print(f"Erro ao criar o banco de dados: {erro}")
        finally:
            self.desconectar()

    def insereAluno(self, ra, imagem_bytes):
        try:
            self.conectar()

            self.cursor.execute('''
        INSERT INTO alunos (ra, foto)
        VALUES (?, ?)
        ''', (ra, sqlite3.Binary(imagem_bytes)))

            self.conexao.commit()
            print("Dados inseridos com sucesso.")

        except sqlite3.Error as erro:
            print(f"Erro ao inserir dados: {erro}")

        finally:
            self.desconectar()

    def atualiza_presenca(self, ra, presente):
        try:
            self.conectar()
            self.cursor.execute('''
        INSERT INTO presencas (ra, data_hora, presente)
            VALUES (?, strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime'), ?)
        ''', (ra, presente))
            self.conexao.commit()
            print("Presença atualizada com sucesso.")
        except sqlite3.Error as erro:
            print(f"Erro ao atualizar dados: {erro}")
        finally:
            self.desconectar()


    def consultaAlunos(self):
        try:
            self.conectar()
            self.cursor.execute('SELECT * FROM alunos')
            alunos = self.cursor.fetchall()
            for aluno in alunos:
                print(aluno)
        except sqlite3.Error as erro:
            print(f"Erro ao consultar dados: {erro}")
        finally:
            self.desconectar()

    def consultaAlunoPorRA(self, ra):
        try:
            self.conectar()
            self.cursor.execute('''
            SELECT ra FROM alunos
            WHERE ra = ?
            ''', (ra,))
            aluno = self.cursor.fetchone()
            if aluno:
                return aluno[0]
            else:
                print("Aluno não encontrado.")

        except sqlite3.Error as erro:
            print(f"Erro ao consultar aluno por RA: {erro}")

        finally:
            self.desconectar()

    def consultaFotoAlunoPorRA(self, ra):
        try:
            print(f"Ra: {ra}")
            self.conectar()
            self.cursor.execute('''
        SELECT foto FROM alunos
        WHERE ra = ?
        ''', (ra,))
            aluno = self.cursor.fetchone()
            if aluno:
                print("Aluno encontrado.")
                return aluno[0]
            else:
                print("Aluno não encontrado.")
                return None

        except sqlite3.Error as erro:
            print(f"Erro ao consultar foto aluno por RA: {erro}")
            return None

        finally:
            self.desconectar()
