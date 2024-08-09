import zmq
import json

goals = {}

def set_goal(data):
    goals[data['category']] = data['amount']
    return {"message": "Goal set successfully"}

def check_goal(data):
    category = data['category']
    spent = data['spent']
    if category not in goals:
        return {"error": "No goal set for this category"}
    goal = goals[category]
    remaining = goal - spent
    return {
        "goal": goal,
        "spent": spent,
        "remaining": remaining,
        "status": "On track" if remaining > 0 else "Exceeded"
    }

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("ipc:///tmp/goal_tracker")

while True:
    message = socket.recv_json()
    if message['action'] == 'set_goal':
        response = set_goal(message['data'])
    elif message['action'] == 'check_goal':
        response = check_goal(message['data'])
    else:
        response = {"error": "Unknown action"}
    socket.send_json(response)
