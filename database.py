import sqlite3

class Database:
    def __init__(self, data):
        self.name = data + '.db'
        self.conn = sqlite3.connect(data + '.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY, title TEXT,content TEXT NOT NULL);")
    
    def add(self, note):
        insert_query = ("INSERT INTO note (title, content) VALUES (?, ?)")
        values = (note.title, note.content)
        self.cursor.execute(insert_query, values)
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        lista = []
        for linha in cursor:
            identificador = linha[0]
            nome_da_rua = linha[1]
            cpf = linha[2]
            note = Note(identificador, nome_da_rua, cpf)
            
            lista.append(note)
        
        return lista
    
    def update(self, note):
        update_query = ("UPDATE note SET title = ?, content = ? WHERE id = ?")
        values = (note.title, note.content, note.id)
        self.cursor.execute(update_query, values)
        self.conn.commit()
    
    def delete(self, note_id):
        delete_query = ("DELETE FROM note WHERE id = ?")
        values = (note_id,)
        self.cursor.execute(delete_query, values)
        self.conn.commit()

class Note:
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content