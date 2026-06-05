from pypdf import PdfReader
from typing import List

class PDFLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> List[str]:
        reader = PdfReader(self.file_path)
        text = []
        for page in reader.pages:
            text.append(page.extract_text())
        return text
    