import os
import requests

# Busca o Token das variáveis de ambiente / Secrets do GitHub
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = "1147312591"


def enviar_lembrete():
  if not TELEGRAM_TOKEN:
    print("Erro: TELEGRAM_TOKEN não configurado!")
    return

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