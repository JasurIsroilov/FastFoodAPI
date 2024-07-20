import os
from dotenv import load_dotenv


load_dotenv()


class DatabaseConfig:
    name: str = os.getenv("DB_NAME")
    username: str = os.getenv("DB_USERNAME")
    password: str = os.getenv("DB_PASSWORD")
    host: str = os.getenv("DB_HOST")
    port: str = os.getenv("DB_PORT")


class JWTConfig:
    REFRESH_TOKEN_LIFETIME = int(os.getenv("REFRESH_TOKEN_LIFETIME"))
    ACCESS_TOKEN_LIFETIME = int(os.getenv("ACCESS_TOKEN_LIFETIME"))


class Config:
    DEBUG: bool = True if os.getenv("DEBUG") == "1" else False
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    HOST: str = os.getenv("HOST")
    database: DatabaseConfig = DatabaseConfig()
    jwt_config: JWTConfig = JWTConfig()
