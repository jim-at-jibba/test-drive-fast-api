from fastapi import FastAPI, Depends

from app.config import get_settings, Settings


app = FastAPI()

# Take note of settings: Settings = Depends(get_settings).
# Here, the Depends function is a dependency that declares another dependency,
# get_settings. Put another way, Depends depends on the result of get_settings.
# The value returned, Settings, is then assigned to the settings parameter.
#
# FastApi has async built in


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }
