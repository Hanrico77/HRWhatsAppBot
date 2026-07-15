import requests
import config


class WhatsAppService:

    def send_text(self, to_number, message):

        url = (
            f"https://graph.facebook.com/"
            f"{config.GRAPH_API_VERSION}/"
            f"{config.PHONE_NUMBER_ID}/messages"
        )

        headers = {
            "Authorization": f"Bearer {config.META_ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }

        payload = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "text",
            "text": {
                "body": message
            }
        }

        response = requests.post(
            url,
            headers=headers,
            json=payload
        )

        print("Status:", response.status_code)
        print(response.text)

        return response