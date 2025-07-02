from pydantic_settings import BaseSettings, SettingsConfigDict
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    BITLY_API: str = "Your API Key"
    # MAIN WINDOW SETTINGS
    ROOT_GEOMETRY: str = "550x330"
    ROOT_RESIZABLE: tuple = (False, False)
    ROOT_TITLE: str = 'Link Trimmer for YouTube/YouTube Music links'
    ROOT_ICON: str = resource_path("assets/icon.ico")
    # BUTTONS SIZES, BORDERS AND POSITIONS
    BUTTON_WIDTH: int = 25
    BUTTON_BORDER_WIDTH: str = "3"
    X_ROW_ONE: int = 70
    X_ROW_TWO: int = 300
    Y_COL_ONE: int = 160
    Y_COL_TWO: int = 230
    # TEXT COLOR FOR COLORED BUTTONS
    FOREGROUND_COLOR: str = "mint cream"
    # COLORS OF THE COLORED BUTTONS
    COLORED_BUTTON_ONE: str = "forest green"
    COLORED_BUTTON_TWO: str = "SteelBlue3"


def get_settings() -> Settings:
    return Settings()