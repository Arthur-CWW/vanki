from fastapi import FastAPI

app = FastAPI()
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl

# class Settings(BaseSettings):
#     database_url: AnyHttpUrl
#     nextauth_url: AnyHttpUrl
#     model_config = S

from pydantic_settings import BaseSettings, SettingsConfigDict

from pydantic.env_settings import build_from_env


class Settings(BaseSettings):
    # nextauth_url: AnyHttpUrl
    model_config = SettingsConfigDict(env_file='../.env', env_file_encoding='utf-8')
    database_url: AnyHttpUrl



@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}
