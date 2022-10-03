from typing import Any

from fastapi import FastAPI

from vercel_fastapi.server.routes import router


app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root() -> dict[str, Any]:
    return {
        "message": "Welcome to my notes application, use the /docs route to proceed"
    }


app.include_router(router, prefix="/note")
