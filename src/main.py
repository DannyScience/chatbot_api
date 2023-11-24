from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chatbot.chatbot import execute_promt

app = FastAPI(
    title="ChatBot"
)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)


@app.get("/send_promt")
def send_promt(promt: str):
    response = execute_promt(promt)
    return {"status": 200, "data": response}
