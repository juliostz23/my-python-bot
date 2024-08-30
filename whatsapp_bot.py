import os
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

@app.route("/bot", methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()

    if 'stage' not in session:
        session['stage'] = 1

    if session['stage'] == 1:
        msg.body("Prazer, GV1! Somos uma agência especializada no marketing de influência, trazendo soluções personalizadas para sua marca 💜")
        session['stage'] = 2

    elif session['stage'] == 2:
        msg.body("Qual é a sua marca?")
        session['stage'] = 3

    elif session['stage'] == 3:
        session['marca'] = incoming_msg
        msg.body("Qual é o seu site e/ou Instagram?")
        session['stage'] = 4

    elif session['stage'] == 4:
        session['site_instagram'] = incoming_msg
        msg.body("O que você procura com a divulgação pelo nosso time de influenciadores?")
        session['stage'] = 5

    elif session['stage'] == 5:
        session['objetivo'] = incoming_msg
        msg.body("Obrigado por fornecer as informações! A GV1 entrará em contato em breve.")
        session.clear()

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
