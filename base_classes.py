import pydantic

class Keys(pydantic.BaseSettings):
    db_name: str
    db_login: str
    db_pass: str
    telebot_token: str
    weather_api_key: str
