from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    users.append(data)
    return jsonify({'message': 'Utilisateur enregistré avec succès'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    for user in users:
        if user['username'] == data['username'] and user['password'] == data['password']:
            return jsonify({'message': 'Connexion réussie'}), 200
    return jsonify({'message': 'Échec de la connexion'}), 401

if __name__ == '__main__':
    app.run(port=5000)