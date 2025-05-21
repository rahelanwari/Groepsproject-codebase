from flask import Blueprint, request, jsonify
from supabase_client import supabase


api_bp = Blueprint('api', __name__)

@api_bp.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(
        id=data['id'],
        display_name=data['display_name'],
        public_key=data['public_key']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@api_bp.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({
        'id': user.id,
        'display_name': user.display_name,
        'public_key': user.public_key
    })
