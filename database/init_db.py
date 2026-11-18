from database.connection import conectar
def criar_banco():
 c=conectar();cur=c.cursor();
 cur.execute("CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT,usuario TEXT,senha TEXT)");
 cur.execute("CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT,telefone TEXT,email TEXT)");
 cur.execute("CREATE TABLE IF NOT EXISTS profissionais(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT,especialidade TEXT)");
 cur.execute("CREATE TABLE IF NOT EXISTS servicos(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT,valor REAL,duracao INTEGER)");
 cur.execute("CREATE TABLE IF NOT EXISTS agendamentos(id INTEGER PRIMARY KEY AUTOINCREMENT,cliente TEXT,profissional TEXT,servico TEXT,data TEXT,horario TEXT)");
 cur.execute("INSERT OR IGNORE INTO usuarios(id,usuario,senha) VALUES(1,'admin','123456')"); c.commit(); c.close()
