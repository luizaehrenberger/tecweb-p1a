import json
from database import Database

def extract_route(string):
    return string.split(' ')[1].lstrip('/')

def read_file(filepath):
    with open(filepath, 'rb') as f:
        return f.read()

def load_data():
    db = Database('banco')
    return db.get_all()


def load_template(template):
    with open("templates/" + template, 'r', encoding='utf-8') as archive:
        html = archive.read()
    return html

def write_on_file(path, dict):
    with open("data/" + path, 'r') as archive:
        texto = archive.read()
    dicionario = json.loads(texto)
    dicionario.append(dict)

def build_response(body='', code=200, reason='OK', headers=''):
    if headers == '':
        response = "HTTP/1.1 " + str(code) + " " + reason + "\n\n" + body
    else:
        response = "HTTP/1.1 " + str(code) + " " + reason + "\n" + headers + "\n\n" + body
    
    return str(response).encode()
