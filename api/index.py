# from fastapi import FastAPI

# app = FastAPI()
# from pydantic_settings import BaseSettings
# from pydantic import AnyHttpUrl

# class Settings(BaseSettings):
#     database_url: AnyHttpUrl
#     nextauth_url: AnyHttpUrl
#     model_config = S

from pydantic import AnyHttpUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    # nextauth_url: AnyHttpUrl
    model_config = SettingsConfigDict(env_file='../.env', env_file_encoding='utf-8')
    DATABASE_URL: Field(AnyHttpUrl, env='DATABASE_URL')

from litestar import Litestar, get
#

# @app.get("/api/python")
# def hello_world():
#     return {"message": "Hello World"}

@get("/")
async def index() -> str:
    # return "Hello, world!"
    settings = Settings()
    print(settings.model_config)
    print(settings)
    return settings.model_dump_json()


@get("/books/{book_id:int}")
async def get_book(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}


app = Litestar([index, get_book])
