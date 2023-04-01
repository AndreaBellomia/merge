from datetime import datetime, timedelta
import random
import json

import subprocess
import os


directory_name = 'fixtures'
script_path = './manage.py'

data_range_start = datetime.now() + timedelta(days=1)
data_range_end = datetime.now() + timedelta(days=30)


pk_booking = 0


array = []
list_srt_state = ['FREE', 'WAIT', 'BLOCK']


def sort_array(obj):
    return (obj['model'], obj['pk'])


# Genera gli appuntamenti collegati a booking
for i in range(1,25):
    random_seconds = random.randint(0, int((data_range_end - data_range_start).total_seconds()))
    random_date = data_range_start + timedelta(seconds=random_seconds)

    start_time = random_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    end_time = (random_date + timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ")

    random_state = random.randrange(0,3)


    array.append({
        "model": "booking.appointments",
        "pk": i,
        "fields": {
            "owner": 1,
            "start_time": start_time,
            "end_time": end_time,
            "active": True,
            "state": list_srt_state[random_state]
        }
    })

    array.append({
        "model": "booking.booking",
        "pk": i,
        "fields": {
            "description": "App autogenerato descrizione",
            "type": "App auto gen",
            "state": list_srt_state[random_state],
            "available": True,
            "start_time": start_time,
            "end_time": end_time,
            "prenotation_time": "2023-03-30T20:36:43.980Z",
            "appointments": 1,
            "commiter": 1
        }
    })

# Genera gli appuntamenti singoli
for i in range(25,50):
    random_seconds = random.randint(0, int((data_range_end - data_range_start).total_seconds()))
    random_date = data_range_start + timedelta(seconds=random_seconds)

    start_time = random_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    end_time = (random_date + timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ")

    array.append({
        "model": "booking.appointments",
        "pk": i,
        "fields": {
            "owner": 1,
            "start_time": start_time,
            "end_time": end_time,
            "active": True,
            "state": "FREE"
        }
    })


sorted_array  = sorted(array, key=sort_array)


if not os.path.exists(directory_name):
    os.makedirs(directory_name)

with open('./fixtures/booking.json', 'w') as file:
    json.dump(sorted_array, file)


python_command = f'python {script_path} loaddata ./fixtures/booking.json'
subprocess.run(python_command, shell=True)