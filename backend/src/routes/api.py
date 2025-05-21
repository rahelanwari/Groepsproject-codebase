from flask import Blueprint, request, jsonify
from supabase_client import supabase

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    response = supabase.table('users').insert({
        'id': data['id'],
        'cryptnext_id': data['cryptnext_id'],
        'display_name': data['display_name'],
        'mnemonic_phrase': data['mnemonic_phrase'],
        'created_at': data['created_at']
    }).execute()
    if response.error:
        return jsonify({'error': str(response.error)}), 400
    return jsonify({'message': 'User created successfully'}), 201

@api_bp.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    response = supabase.table('users').select("*").eq('id', user_id).single().execute()
    if response.error or not response.data:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(response.data)
