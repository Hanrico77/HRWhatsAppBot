from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse
import json
import config

from services.whatsapp_service import WhatsAppService

router = APIRouter()

service = WhatsAppService()


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

    return {"status": "received"}


