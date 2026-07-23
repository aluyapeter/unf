from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    # DEBUG: bool = False
    # API_PORT: int = 8000
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
