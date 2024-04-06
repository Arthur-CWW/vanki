from fastapi import FastAPI
from pydantic import AnyHttpUrl, AnyUrl, BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict



from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: AnyUrl= Field(default=...)
    nextauth_url: AnyHttpUrl= Field(default=...)
    # model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'



class Card(BaseModel):
    id: int
    name: str
    description: str


app = FastAPI()

@app.get("/")
async def index() -> dict:
    settings = Settings()
    print(settings.database_url, settings.nextauth_url, settings.model_config)
    return settings.model_dump( )

@app.post("/cards", response_model=Card)
async def create_card(card: Card) -> Card:
    print(card)
    return card

@app.get("/cards/{card_id}", response_model=Card)
async def get_cards(card_id: int) -> Card:
    return Card(id=card_id, name="Card", description="Card description")
