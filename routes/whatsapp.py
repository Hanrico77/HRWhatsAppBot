from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse
import json
import config

from services.whatsapp_service import WhatsAppService
from services.command_service import CommandService

router = APIRouter()

whatsapp_service = WhatsAppService()
command_service = CommandService()


@router.get("/webhook")
async def verify_webhook(request: Request):

    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == config.VERIFY_TOKEN:
        return PlainTextResponse(challenge)

    return PlainTextResponse("Verification failed", status_code=403)


@router.post("/webhook")
async def receive_message(request: Request):

    body = await request.json()

    print("=" * 80)
    print("WEBHOOK RECEIVED")
    print(json.dumps(body, indent=4))
    print("=" * 80)

    try:
        value = body["entry"][0]["changes"][0]["value"]

        # Ignore status updates
        if "messages" not in value:
            return {"status": "ignored"}

        message = value["messages"][0]
        sender = message["from"]

        # Only process text messages for now
        if message.get("type") != "text":
            whatsapp_service.send_text(
                sender,
                "⚠️ Only text messages are currently supported."
            )
            return {"status": "received"}

        text = message["text"]["body"]

        print(f"Incoming message: {text}")

        # Execute the command
        response = command_service.execute(text)

        print("Bot response:")
        print(response)

        # Send the reply back to WhatsApp
        whatsapp_service.send_text(sender, response)

    except Exception as ex:
        print("ERROR:", ex)

    return {"status": "received"}