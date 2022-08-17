from app.settings import Settings
from fastapi import Depends, FastAPI, Query, status
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

settings = Settings()
app = FastAPI()


@app.on_event('startup')
async def startup():
    if settings.debug:
        print(settings)
        

TORTOISE_ORM = {
    "connections": {"default": settings.database_url},
    "apps": {
        "models": {
            "models": ["app.models"],
            "default_connection": "default",
        },
    },
}

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)