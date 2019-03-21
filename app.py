from flask import Flask, jsonify , abort , make_response, request
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

app = Flask(__name__)

catalogo = [
    {
        'id':1,
        'item':'Carrinho',
        'categoria':'Brinquedo',
        'preço':'R$:20,00',
        'quantidade_restante':10
    },
    {
        'id':2,
        'item':'Camisa',
        'categoria':'Vestimenta',
        'preço':'R$:30,00',
        'quantidade_restante':20
    },
    {
        'id':3,
        'item':'Boneca',
        'categoria':'Brinquedo',
        'preço':'R$:25,00',
        'quantidade_restante':12
    },
    {
        'id':4,
        'item':'Notebook',
        'categoria':'Informática',
        'preço':'R$:100,00',
        'quantidade_restante':5
    },
    {
        'id':5,
        'item':'Livro',
        'categoria':'Livraria',
        'preço':'R$:15,00',
        'quantidade_restante':50
    }
]

@auth.get_password
def get_password(username):
    if username == 'Neto':
        return 'testepass'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error':'Unauthorized access'}),403)


@app.route('/api/catalogo', methods=['GET','POST'])
@auth.login_required
def get_itens():
    if request.method == 'GET':
        return jsonify({'catalogo':catalogo})
    elif request.method == 'POST':
        if not request.json or not 'item' in request.json:
            abort(400)
        item = {
            'id':catalogo[-1]['id'] + 1,
            'item':request.json['item'],
            'categoria':request.json.get('categoria',"Categoria não definida"),
            'preço':request.json.get('categoria',"Preço não definido"),
            'quantidade_restante':request.json.get('quantidade_restante',0)
        }
        catalogo.append(item)
        return jsonify({'item':item}) , 201 



@app.route('/api/catalogo/<int:item_id>',methods=['GET','PUT','DELETE'])
def get_item(item_id):
    item = [item for item in catalogo if item['id'] == item_id]
    if len(item) == 0:
            abort(404)
    if  request.method == 'GET':
        return jsonify({'item': item[0]})
    elif request.method == 'PUT':
        if not request.json:
            abort(400)
        if 'item' in request.json and type(request.json['item']) != unicode:
            abort(400)
        if 'categoria' in request.json and type(request.json['categoria']) is not unicode:
            abort(400)
        if 'preço' in request.json and type(request.json['preço']) is not unicode:
            abort(400)
        if 'quantidade_restante' in request.json and type(request.json['quantidade_restante']) is not int:
            abort(400)
        item[0]['item'] = request.json.get('item', item[0]['item'])
        item[0]['categoria'] = request.json.get('categoria', item[0]['categoria'])
        item[0]['preço'] = request.json.get('preço', item[0]['preço'])
        item[0]['quantidade_restante'] = request.json.get('quantidade_restante', item[0]['quantidade_restante'])
        return jsonify({'task': item[0]})
    elif request.method == 'DELETE':
        catalogo.remove(item[0])
        return jsonify({'result': True})
    


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
app.run()