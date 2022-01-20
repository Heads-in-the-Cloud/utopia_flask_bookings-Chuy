import random
import math
import requests
import json
from faker      import Faker
from datetime   import timedelta
from datetime   import datetime
from src.models    import *                                                                                       


fake = Faker()
PORT = 5001
apiRoute = f'http://localhost:{PORT}/bookings'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


def populateBookings():
    
    def generateCode():
        digits = "0123456789"
        confirmationCode = ""
        for i in range(8) :
            confirmationCode += digits[math.floor(random.random() * 10)]
        return confirmationCode
        
    for i in range(100):
        booking = []
        booking.append({
            "is_active": fake.pyint(min_value=1, max_value=3, step=1),
            "confirmation_code": generateCode()
            
        })
        for i in range(len(booking)):
            r = requests.post(apiRoute, data=json.dumps(booking[i]), headers=headers)
            print(r.status_code)

populateBookings()

    



