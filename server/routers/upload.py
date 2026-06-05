from fastapi import APIRouter
from services.pdf_loader import PDFLoader


router = APIRouter(
    prefix="/upload",
    tags=["upload"]
)


@router.post("/upload/")
async def upload_pdf(file_path: str):
    try:
        pdf_loader = PDFLoader(file_path)
        text = pdf_loader.load()
        return {"text": text}
    except Exception as e:
        return {"error": str(e)}