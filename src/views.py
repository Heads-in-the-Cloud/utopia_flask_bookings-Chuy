# Flask/Python Packages
from flask import request, jsonify, make_response
from . import app
from .models.booking import *                                                                 
import json
from .database import *
    
    
@app.route('/bookings', methods = ['POST', 'GET'])
def getBookings():
    if request.method == 'GET':
        bookings = Booking.query.all()
        all_bookings = []
        for booking in bookings:                                                 
            new_bookings = {
                 "id": booking.id,
                 "is_active": booking.is_active,
                 "confirmation_code": booking.confirmation_code
             }
            all_bookings.append(new_bookings)
        return json.dumps(all_bookings), 200
    
    if request.method == 'POST':
        data = request.get_json()
        is_active = data['is_active']
        confirmation_code = data['confirmation_code']
        booking = Booking(is_active=is_active, confirmation_code=confirmation_code)
        db.session.add(booking)
        db.session.commit()
        return json.dumps("Added Booking"), 200
    
    else:
        return "Error", 500






