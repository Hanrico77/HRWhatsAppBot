from fastapi import APIRouter

from services.command_service import CommandService

router = APIRouter()

service = CommandService()


@router.get("/command")
async def command(cmd: str):

    return service.execute(cmd)