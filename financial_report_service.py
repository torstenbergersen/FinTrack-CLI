import zmq
import json
from collections import defaultdict

def generate_report(transactions):
    total_spending = sum(t['amount'] for t in transactions)
    category_spending = defaultdict(float)
    for t in transactions:
        category_spending[t['category']] += t['amount']
    
    report = {
        "total_spending": total_spending,
        "category_breakdown": dict(category_spending)
    }
    return report

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("ipc:///tmp/financial_report")

while True:
    message = socket.recv_json()
    if message['action'] == 'generate_report':
        report = generate_report(message['data'])
        socket.send_json(report)
    else:
        socket.send_json({"error": "Unknown action"})
