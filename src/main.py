from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chatbot.chatbot import execute_promt
from fastapi_users import FastAPIUsers, fastapi_users
from auth.auth import auth_backend
from auth.schemas import UserCreate, UserRead
from auth.database import User
from auth.manager import get_user_manager

app = FastAPI(
    title="ChatBot"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
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
