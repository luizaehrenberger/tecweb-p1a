
from utils import extract_route, read_file, load_data, load_template, write_on_file, build_response
from database import Database
from database import Note
import urllib.parse

def index(request):
    db = Database('data/banco')
    
    if request.startswith('POST'):
        partes = request.split('\n\r\n')
        print(partes)
        corpo = partes[1]
        params = {}
        parametros_brutos = corpo

        print('/'*100)
        print(parametros_brutos)
        print('/'*100)
        for chave_valor in parametros_brutos.split('&'):
            # AQUI É COM VOCÊ
            print(chave_valor.split('='))
            chave, valor = chave_valor.split('=')
            print(chave)
            print(valor)
            
            params[chave] = urllib.parse.unquote_plus(valor)
            if chave == 'titulo':
                titulo = urllib.parse.unquote_plus(valor)
                print(titulo)
            elif chave == 'detalhes':
                conteudo = urllib.parse.unquote_plus(valor)
                print(conteudo)
        
        lista = db.get_all()
        for notes in lista:
            if notes.title == titulo or notes.content == conteudo:
                db.delete(notes.id)
                print("deletou")
        db.add(Note(title=titulo, content=params[chave]))

        return build_response(code = 303, reason = 'See Other', headers = 'Location: /')
    
    notes_template = load_template('components/note.html')
    notes_li = [
        notes_template.format(title=dados.title, details=dados.content, id=dados.id)
        for dados in db.get_all()
        ]
    notes = '\n'.join(notes_li)
    
    return build_response(body=load_template('index.html').format(notes=notes))
    
    

