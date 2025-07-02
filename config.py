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
    BUTTON_BORDER_WIDTH: str = "3"
    X_ROW_ONE: int = 70
    X_ROW_TWO: int = 300
    Y_COL_ONE: int = 160
    Y_COL_TWO: int = 230


def get_settings() -> Settings:
    return Settings()