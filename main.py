import time
import requests
import schedule

# Configurações do seu bot
TELEGRAM_TOKEN = "8955435133:AAHA_G_frQF8-dg4Rmo29FTgTAoaqgGWZ90"
CHAT_ID = "1147312591"  # Pode obter enviando uma mensagem para o bot @userinfobot

def enviar_lembrete():
    mensagem = "💧 *Hora de beber água!* Mantenha-se hidratado."
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": mensagem,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

# Agendamento de teste para às 22:13
schedule.every().day.at("22:13").do(enviar_lembrete)

print("Bot de lembrete iniciado...")

while True:
    schedule.run_pending()
    time.sleep(60)