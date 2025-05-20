from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String(6), primary_key=True)
    display_name = db.Column(db.String(50), nullable=False)
    public_key = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # Relaties naar andere modellen (voorbeeld)
    sent_messages = db.relationship('Chat', backref='sender', foreign_keys='Chat.sender_id')
    received_messages = db.relationship('Chat', backref='recipient', foreign_keys='Chat.recipient_id')
