import os
import csv
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

clientes = []

# Certifique-se de que a pasta CADASTRO existe
if not os.path.exists('CADASTRO'):
    os.makedirs('CADASTRO')

@app.route('/')
def index():
    return render_template('index.html', clientes=clientes)

@app.route('/add', methods=['POST'])
def add_cliente():
    nome = request.form['nome']
    cpf = request.form['cpf']
    cep = request.form['cep']
    endereco = request.form['endereco']
    numero = request.form['numero']
    complemento = request.form['complemento']
    cidade = request.form['cidade']
    estado = request.form['estado']
    profissao = request.form['profissao']
    
    cliente = {
        'nome': nome,
        'cpf': cpf,
        'cep': cep,
        'endereco': endereco,
        'numero': numero,
        'complemento': complemento,
        'cidade': cidade,
        'estado': estado,
        'profissao': profissao
    }
    
    clientes.append(cliente)
    salvar_cliente_no_log(cliente)
    return redirect(url_for('index'))

@app.route('/log', methods=['POST'])
def log_cliente():
    cliente = request.get_json()
    salvar_cliente_no_log(cliente)
    return jsonify({'status': 'success'})

def salvar_cliente_no_log(cliente):
    with open('CADASTRO/clientes.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([cliente['nome'], cliente['cpf'], cliente['cep'], cliente['endereco'], cliente['numero'], cliente['complemento'], cliente['cidade'], cliente['estado'], cliente['profissao']])

if __name__ == '__main__':
    app.run(debug=True)
