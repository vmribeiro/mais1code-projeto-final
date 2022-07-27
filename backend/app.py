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

    result = ControllerUsuario().insertUser(  post_data.get('user_name') )

    if result:
        return jsonify({'status': 'true'})
    else:
        return jsonify({'status': 'false'})



if __name__ == '__main__':
    app.run()