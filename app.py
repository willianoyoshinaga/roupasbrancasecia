import os
import csv
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Necessário para usar flash messages

clientes = []

# Certifique-se de que a pasta CADASTRO existe
if not os.path.exists('CADASTRO'):
    os.makedirs('CADASTRO')
    print("Pasta CADASTRO criada")

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
    
    # Validação simples
    if not nome or not cpf ou not cep ou not endereco ou not numero ou not cidade ou not estado:
        flash("Todos os campos obrigatórios devem ser preenchidos", "error")
        return redirect(url_for('index'))
    
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
    try:
        salvar_cliente_no_log(cliente)
        flash("Cadastro concluído com sucesso!", "success")
    except Exception as e:
        flash(f"Erro ao salvar o cadastro: {str(e)}", "error")
    return redirect(url_for('index'))

@app.route('/log', methods=['POST'])
def log_cliente():
    cliente = request.get_json()
    try:
        salvar_cliente_no_log(cliente)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
    return jsonify({'status': 'success'})

def salvar_cliente_no_log(cliente):
    try:
        with open('CADASTRO/clientes.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([cliente['nome'], cliente['cpf'], cliente['cep'], cliente['endereco'], cliente['numero'], cliente['complemento'], cliente['cidade'], cliente['estado'], cliente['profissao']])
        print("Cliente salvo no log")
    except Exception as e:
        print(f"Erro ao salvar cliente no log: {str(e)}")
        raise

if __name__ == '__main__':
    app.run(debug=True)

