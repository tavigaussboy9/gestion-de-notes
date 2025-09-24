from flask import Flask, request, jsonify

app = Flask(__name__)

notes = []

@app.route('/notes', methods=['POST'])
def create_note():
    note = request.json
    notes.append(note)
    return jsonify({'message': 'Note créée avec succès'}), 201

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes), 200

@app.route('/notes/<int:id>', methods=['PUT'])
def update_note(id):
    data = request.json
    if id < len(notes):
        notes[id] = data
        return jsonify({'message': 'Note mise à jour avec succès'}), 200
    return jsonify({'message': 'Note non trouvée'}), 404

@app.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    if id < len(notes):
        notes.pop(id)
        return jsonify({'message': 'Note supprimée avec succès'}), 200
    return jsonify({'message': 'Note non trouvée'}), 404

if __name__ == '__main__':
    app.run(port=5001)