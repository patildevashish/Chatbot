from fastapi import APIRouter, HTTPException
from services.rag import ChatService

chat_service = ChatService()

router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)

@router.post("/message")
async def send_message(message: str):
    try:
        response = chat_service.get_chat_response(message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))