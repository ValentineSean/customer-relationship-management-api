import traceback

from flask import Blueprint, jsonify, request
from models.messages import Message

get_messages_blueprint = Blueprint("get_messages_blueprint", __name__)

@get_messages_blueprint.route("/get-messages")
def get_messages():
    issue_id = request.args.get("issue_id")

    try:
        messages = Message.find((Message.issue==issue_id)&(Message.record_status=="ALIVE")).all()

        messages_list = []

        sender_data = {}
        issue_data = {}

        # JSONIFY REDIS DATA RESPONSE
        for message in messages:
            message_dict = {}
            
            for x in message:
                message_dict[x[0]] = x[1]

            # JSONIFY SENDER DATA IN MESSAGE
            for i in message_dict["sender_data"]:
                sender_data[i[0]] = i[1]

            message_dict["sender_data"] = sender_data

            # JSONIFY ISSUE DATA IN MESSAGE
            for i in message_dict["issue_data"]:
                issue_data[i[0]] = i[1]

            message_dict["issue_data"] = issue_data
                
            messages_list.append(message_dict)
        
        return jsonify({
            "status_code": "200",
            "status": "success",
            "message": "messages_retrieved_ok",
            "data": messages_list
        })

    except:
        traceback.print_exc()
        return jsonify({
            "status_code": "500",
            "status": "error",
            "message": "failed_to_retrieve_messages",
            "data": [],
        })