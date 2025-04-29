from flask import Blueprint, request, jsonify, session
from gpt_logic import build_prompt_and_call_gpt

routes = Blueprint("routes", __name__)

@routes.route("/chat", methods=["POST"])
def chat():
    if 'username' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "Пустой запрос."})

    try:
        response = build_prompt_and_call_gpt(user_message)
        return jsonify({"reply": response})
    except Exception as e:
        return jsonify({"reply": f"Ошибка: {e}"}), 500
