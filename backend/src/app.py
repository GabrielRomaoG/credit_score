from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from kink import di
from src.ml_models.bootstrap import ml_models_bootstrap_di
from src.routes.predict import predict
from src.service.bootstrap import service_bootstrap_di


@asynccontextmanager
async def lifespan(app: FastAPI):
    ml_models_bootstrap_di()
    service_bootstrap_di()
    yield

    di.clear_cache()


app = FastAPI(lifespan=lifespan)


app.include_router(predict.router)


@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")
