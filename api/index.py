# from fastapi import FastAPI

# app = FastAPI()
# from pydantic_settings import BaseSettings
# from pydantic import AnyHttpUrl

# class Settings(BaseSettings):
#     database_url: AnyHttpUrl
#     nextauth_url: AnyHttpUrl
#     model_config = S

from pydantic import AnyHttpUrl, AnyUrl, BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict



from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: AnyUrl
    nextauth_url: AnyHttpUrl
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')



from litestar import Litestar, get, post, put, delete


@get("/")
async def index() -> str:
    settings = Settings() # type: ignore

    print(settings.database_url, settings.nextauth_url, settings.model_config)
    return settings.model_dump_json( )

# from dataclasses import dataclass

class Card(BaseModel):
    id: int
    name: str
    description: str



@post("/cards")
def create_card(card: Card) -> Card:
    print(card)
    return card

@get("/cards/{card}")
def get_cards(numb: int) -> Card:
    return Card(id=numb, name="Card", description="Card description")
app = Litestar([index, create_card])
