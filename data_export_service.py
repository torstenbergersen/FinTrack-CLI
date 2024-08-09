import zmq
import json
import csv
from io import StringIO

def export_to_csv(transactions):
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=["id", "date", "amount", "category"])
    writer.writeheader()
    for transaction in transactions:
        writer.writerow(transaction)
    return output.getvalue()

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("ipc:///tmp/data_export")

while True:
    message = socket.recv_json()
    if message['action'] == 'export_csv':
        csv_data = export_to_csv(message['data'])
        socket.send_json({"csv_data": csv_data})
    else:
        socket.send_json({"error": "Unknown action"})
