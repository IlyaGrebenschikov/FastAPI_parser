import secrets
from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath
from sqlalchemy import URL


class EnvSettings(BaseSettings):
    root_dir: DirectoryPath = Path(__file__).parent.parent.parent
    model_config = SettingsConfigDict(
        env_file=f'{root_dir}/.env',
        env_file_encoding='utf-8',
    )

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str


class DBSettings(EnvSettings):
    def create_url_obj(self) -> URL:
        url_obj = URL.create(
            'postgresql+asyncpg',
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            database=self.POSTGRES_DB,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT
        )
        return url_obj

    @property
    def get_url(self) -> str:
        return self.DB_URL.format(
            POSTGRES_USER=self.POSTGRES_USER,
            POSTGRES_PASSWORD=self.POSTGRES_PASSWORD,
            POSTGRES_HOST=self.POSTGRES_HOST,
            POSTGRES_PORT=self.POSTGRES_PORT,
            POSTGRES_DB=self.POSTGRES_DB,
        )


class SecretSettings:
    secret_key: str = secrets.token_hex(32)
    secret_algh: str = 'HS256'


class Settings:
    db: DBSettings = DBSettings()
    secret: SecretSettings = SecretSettings()


@lru_cache(typed=True)
def get_settings() -> Settings:
    return Settings()
