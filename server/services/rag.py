from google import genai
import os
import dotenv

dotenv.load_dotenv()

selectedmodel = os.getenv("GOOGLE_MODEL", "gemini-2.5-flash")
class ChatService:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GOOGLE_API_KEY")
        )

    def get_chat_response(self, message: str) -> str:
        try:
            response = self.client.models.generate_content(
                model=selectedmodel,
                contents=message
            )
        except Exception as e:
            print(f"Error generating chat response: {e}")
            raise

        return response.text