# from fastapi import FastAPI

# app = FastAPI()
# from pydantic_settings import BaseSettings
# from pydantic import AnyHttpUrl

# class Settings(BaseSettings):
#     database_url: AnyHttpUrl
#     nextauth_url: AnyHttpUrl
#     model_config = S

from pydantic import AnyHttpUrl, AnyUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict



from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: AnyUrl
    nextauth_url: AnyHttpUrl
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')



from litestar import Litestar, get
#

# @app.get("/api/python")
# def hello_world():
#     return {"message": "Hello World"}

@get("/")
async def index() -> str:
    settings = Settings() # type: ignore

    print(settings.model_config)
    return settings.model_dump_json( )


@get("/books/{book_id:int}")
async def get_book(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}


app = Litestar([index, get_book])
