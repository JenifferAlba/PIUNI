from flask import Blueprint, request, jsonify
from models import db, Appointment

api = Blueprint('api', __name__)

@api.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    new_appt = Appointment(
        name=data['name'],
        phone=data['phone'],
        email=data['email'],
        service=data['service'],
        date=data['date'],
        time=data['time']
    )
    db.session.add(new_appt)
    db.session.commit()
    return jsonify({'message': 'Agendamento salvo com sucesso!'}), 201