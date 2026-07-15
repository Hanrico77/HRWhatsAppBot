from fastapi import FastAPI
from routes.whatsapp import router as whatsapp_router

import config

from routes.health import router as health_router
from routes.employee import router as employee_router



app = FastAPI(

    title=config.APP_NAME,

    version=config.APP_VERSION

)

app.include_router(health_router)

app.include_router(employee_router)

app.include_router(whatsapp_router)

@app.get("/")
def root():

    return {

        "Application": config.APP_NAME,

        "Version": config.APP_VERSION,

        "Status": "Running"

    }