from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import chat, upload, users

app = FastAPI(title="College Chatbot API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router)
app.include_router(chat.router)
app.include_router(upload.router)


@app.get("/")
async def root():
    return {"message": "College Chatbot API is running"}


