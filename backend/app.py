from flask import Flask, jsonify, request
from flask_cors import CORS
from controller.ControllerUsuario import ControllerUsuario


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
 
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
 
 
################ 
# Inicio Rotas de teste
################

@app.route('/')
def home():
    return jsonify({
        'status': 'success',
        'page': 'home_page'
    })
 

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'members': {'did_it_work': 'Yes!'}
    })

################ 
# Fim das rotas de teste
################


'''
*******************
USERS
*******************
'''


@app.route('/insert_user', methods=['POST'])
def insert_user():
    
    post_data = request.get_json(silent=True)

    result = ControllerUsuario().insertUser(  post_data.get('user_name'),
                                              post_data.get('name'),
                                              post_data.get('data_de_nascimento'),
                                              post_data.get('telefone'),
                                              post_data.get('is_professional'),
                                              post_data.get('formacao'),
                                              post_data.get('especializacao') 
                                              )

    if result:
        return jsonify({'status': 'true'})
    else:
        return jsonify({'status': 'false'})


@app.route('/select_all_users', methods=['GET'])
def select_all_users():

    result = ControllerUsuario().select_all_users()

    if result:
        return jsonify({'status': 'true', 'result': result})
    else:
        return jsonify({'status': 'false'})


@app.route('/select_user_by_id/<string:user_id>', methods=['GET'])
def select_user_by_id(user_id):

    result = ControllerUsuario().select_user_by_id(user_id)

    if result:
        return jsonify({'status': 'true', 'result': result})
    else:
        return jsonify({'status': 'false'})


@app.route('/update_user', methods=['POST'])
def update_user():

    post_data = request.get_json(silent=True)
    
    result = ControllerUsuario().update_user(    post_data.get('user_name') , post_data.get('name') , post_data.get('data_de_nascimento') , post_data.get('telefone') , post_data.get('is_professional') , post_data.get('formacao') , post_data.get('especializacao') , post_data.get ('user_id') )

    if result:
        return jsonify({'status': 'true'})
    else:
        return jsonify({'status': 'false'})



@app.route('/delete_user/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):

    result = ControllerUsuario().delete_user(user_id)

    if result:
        return jsonify({'status': 'true', 'result': 'user deleted'})
    else:
        return jsonify({'status': 'false'})


if __name__ == '__main__':
    app.run()
    