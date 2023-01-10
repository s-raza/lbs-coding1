from pydantic import BaseModel, BaseSettings


class Database(BaseModel):
    sqlite_url: str


class App(BaseModel):
    host: str
    port: int
    debug: bool


class InitData(BaseModel):
    num_meters: int
    max_meters: int
    min_meters: int
    num_meter_readings: int
    max_meter_readings: int
    min_meter_readings: int


class Settings(BaseSettings):
    db: Database
    app: App
    init_data: InitData

    class Config:
        env_file = ".env"
        env_nested_delimiter = "__"


cfg = Settings()
