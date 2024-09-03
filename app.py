from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Ei galera, você fez acesso ao servidor!'

@app.route('/index')
def minha_page():
    print(request.method)
    return render_template('index.html')

@app.route('/qual', methods=['POST'])
def achar_mamae():
    print(request.method)
    nome = request.form.get('namorada')
    if nome is None:
        return "Erro: nome não fornecido!", 400

    if nome.lower() == 'jasmin':
        return render_template('acheimamae.html')
    else:
        return render_template('respostaerrada.html')

if __name__ == '__main__':
    app.run(debug=True)
