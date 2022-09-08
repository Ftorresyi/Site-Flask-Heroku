from flask import Flask, render_template
#render_template faz importar as paginas HTML para o FLASK. Ela procura autmaticamente a pasta template com as pgs HTML.

app = Flask(__name__)  #cria o site no servidor local
# route -> hashtagtreinamentos.com/
# função -> o que você quer exibir naquela página
# template

@app.route("/") #cria uma nova página com o caminho especificado
def homepage():
    #return "Esse é o meu 1° site. " 
    return render_template("homepage.html")

@app.route("/contatos") #cria uma página chamada contatos
def contatos():
    #return "<p>Nossos contatos são: yindiyft@gmail.com</p><p>Telefone: (21)XXXX-XXXX</p>"
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>") #Cria uma página dinamicamente de acordo com o conteudo entre < >
def usuarios(nome_usuario):
    #return nome_usuario
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True) #ativa o debug para automatizar as edições

    # servidor do heroku

#Após isso é necessário criar dois arquivos dentro da mesma pasta:
#requirements.txt, que diz pro FLASK quais bibliotecas instaladas estao sendo usadas pelo Python
#Procfile, Que informa ao Flask o nome do seu site que será rodado
#instalar o gunicorn para isso
#OBS.: O comando pip freeze > requirements.txt captura as libs instaladas e cria o arquivo requirements.txt
