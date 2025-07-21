from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
users = {}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# POST new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = str(len(users) + 1)
    users[user_id] = data
    return jsonify({'id': user_id, 'user': data}), 201

# PUT update user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        users[user_id] = request.get_json()
        return jsonify({'id': user_id, 'user': users[user_id]})
    return jsonify({'error': 'User not found'}), 404

# DELETE user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({'message': f'User {user_id} deleted'})
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
