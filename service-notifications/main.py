from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify_user():
    # Simulate sending notification logic
    return jsonify({'message': 'Notification envoyée avec succès'}), 200

if __name__ == '__main__':
    app.run(port=5002)