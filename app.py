from fastapi import FastAPI
import config

app = FastAPI(
    title=config.APP_NAME,
    version=config.APP_VERSION
)

@app.get("/")
def root():

    return {
        "application": config.APP_NAME,
        "status": "Running"
    }
