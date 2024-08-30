from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Configurações do Twilio
ACCOUNT_SID = 'YOUR_TWILIO_ACCOUNT_SID'
AUTH_TOKEN = 'YOUR_TWILIO_AUTH_TOKEN'
TWILIO_PHONE_NUMBER = 'YOUR_TWILIO_PHONE_NUMBER'

client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.route('/bot', methods=['POST'])
def bot():
    """Recebe mensagens e responde."""
    incoming_msg = request.values.get('Body', '').lower()
    from_number = request.values.get('From')
    
    response = MessagingResponse()
    
    if 'oi' in incoming_msg:
        response.message(f'Olá! Como você está?')
        response.message('Prazer, GV1! Somos uma agência especializada no marketing de influência, trazendo soluções personalizadas para sua marca 💜')
        response.message('Por favor, me diga qual é a sua marca:')
    elif 'marca' in incoming_msg:
        response.message('Obrigado! Agora, por favor, informe o site e/ou Instagram da sua marca:')
    elif 'site' in incoming_msg or 'instagram' in incoming_msg:
        response.message('Entendi! E o que você está procurando com a divulgação pelo nosso time de influenciadores?')
    else:
        response.message('Desculpe, não entendi sua mensagem. Por favor, me diga qual é a sua marca.')

    return str(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
