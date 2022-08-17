from pydantic import BaseSettings

class Settings(BaseSettings):
    debug: bool = True
    environment: str = "development"
    database_url: str = "sqlite://ch10_project.db"
    
    class Config:
        env_file = ".env"