from flask import Flask, render_template
app = Flask(__name__)

USUARIO_LOGADO = "Prof. Xavier"
lista_de_aluno = ["João Victor", "Pedro", "Julia"]

@app.route("/")
def pagina_inicial():
    return render_template('index.html', nome=USUARIO_LOGADO, lista=lista_de_aluno)

@app.route("/autenticacao")
def autenticador():
    usuario_logado = "João Victor"
    admin = True
    materias = ["Matematica", "Historia da web", "HTML", "Programação Web"]
    return render_template('base.html',
                           login=usuario_logado,
                           admin=admin,
                           materias=materias)

DETALHES_DO_SISTEMA = {"versao": 1.5, "data": "2025-10-15"}

@app.route("/info")
def info():
    return render_template('info.html', detalhes=DETALHES_DO_SISTEMA)


@app.route("/nome/<nome_usuario>")
def nome(nome_usuario):
    return render_template('nome.html', nome_url = nome_usuario)



@app.route("/moeda")
def moeda():
 taxa_dolar = 5.25
 valor_real = 100

 valor_dolar = valor_real / taxa_dolar

 return render_template('moeda.html', valor_real = valor_real, valor_dolar = valor_dolar, taxa_dolar = taxa_dolar)


CONFIG = {
    'site_ativo': True, 'limite_usuarios': 50, 'modo_manuntencao': False
    }

@app.route("/config")
def config():
    return render_template('config.html', config = CONFIG)

TURMA = [['Ana', 9.0, 7.5], ['Bruno', 5.0, 6.0]]

@app.route("/turma")
def turma():
    return render_template('turma.html', turma = TURMA)

ESTOQUE = 6

@app.route("/mercado")
def mercado():
    return render_template('estoque.html', estoque = ESTOQUE)

SALA = [
    ['ana', 9.0, 7.5],
    ['Bruno', 5.0, 6.0],
    ['Carlos', 4.5, 5.5]

]


@app.route("/sala")
def sala():
    return render_template('sala.html', sala = SALA)



ALUNOS = {
    'nome': 'João Victor',
    'notas': [9.0, 7.5, 8.0]
}

def calculadora(listas_notas):
    if len(listas_notas) == 0:
     return 0
    return sum(listas_notas) / len(listas_notas)

@app.route("/relatorio")
def relatorio():
    media = calculadora(ALUNOS['notas'])

    return render_template('relatorio.html', aluno = ALUNOS, media = media)


@app.route("/escola/aluno1")
def relatorio_aprovado():
    nome_aluno = "João Victor",
    media_final = 8.5
    return render_template('escola.html', nome=nome_aluno, nota=media_final)

@app.route("/escola/aluno2")
def relatorio_reprovado():
    nome_aluno = "Mario Kuga",
    media_final = 5.8
    return render_template('escola.html', nome=nome_aluno, nota=media_final)
if __name__ == "__main__":
    app.run(debug=True)
