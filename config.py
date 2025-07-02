from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    BITLY_API: str
    ROOT_GEOMETRY: str = "550x330"
    ROOT_RESIZABLE: tuple = (False, False)
    ROOT_TITLE: str = 'Link Trimmer for YouTube/YouTube Music links'
    BUTTON_WIDTH: int = 25
    BUTTON_BD: str = "3"


def get_settings() -> Settings:
    return Settings()