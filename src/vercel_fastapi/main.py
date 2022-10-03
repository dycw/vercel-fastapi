from uvicorn import run


if __name__ == "__main__":
    run(
        "vercel_fastapi.server.api:app",
        host="0.0.0.0",  # noqa: S104
        port=8000,
        reload=True,
        app_dir="src",
    )
