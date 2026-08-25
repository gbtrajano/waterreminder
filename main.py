import requests

TELEGRAM_TOKEN = "8955435133:AAHA_G_frQF8-dg4Rmo29FTgTAoaqgGWZ90"
CHAT_ID = "1147312591"


def enviar_lembrete():
  mensagem = "💧 *Hora de beber água!* Mantenha-se hidratado."
  url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
  payload = {
      "chat_id": CHAT_ID,
      "text": mensagem,
      "parse_mode": "Markdown",
  }
  response = requests.post(url, json=payload)
  print(f"Status do envio: {response.status_code}")


if __name__ == "__main__":
  enviar_lembrete()