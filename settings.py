"""Configuração centralizada — único lugar que lê o .env."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    MCP_API_KEY: str
    PORT: int = 8001

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
