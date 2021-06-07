from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'id':0,
        'nome':'Everton Oliveira',
        'habilidades':['Python','Flask']
     },
    {
        'id':1,
        'nome':'Oliveira Felix',
        'habilidades':['Python','Django']
    }
]

# Retorna registros pelo ID e também atualiza e deleta

@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'Erro','mensagem':mensagem}
        except Exception:
            mensagem = "Erro desconhecido. Procure o administrador da API"
            response = {'status': 'Erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'Sucesso','mensagem':'Registro Excluido!'})

# Lista todos registros e inclui um novo!
@app.route('/dev/', methods=['POST','GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)