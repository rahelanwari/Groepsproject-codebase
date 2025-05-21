from app import supabase
from flask import Blueprint, request, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    # Voeg een nieuwe user toe aan Supabase
    response = supabase.table('users').insert({
        'id': data['id'],
        'display_name': data['display_name'],
        'public_key': data['public_key']
    }).execute()
    # Check op errors
    if response.error:
        return jsonify({'error': response.error.message}), 400
    return jsonify({'message': 'User created successfully', 'user': response.data[0]}), 201

@api_bp.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    # Haal user op uit Supabase obv id
    response = supabase.table('users').select('*').eq('id', user_id).single().execute()
    if response.error or not response.data:
        return jsonify({'error': 'User not found'}), 404
    user = response.data
    return jsonify({
        'id': user['id'],
        'display_name': user['display_name'],
        'public_key': user['public_key']
    })
