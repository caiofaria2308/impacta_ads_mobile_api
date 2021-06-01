from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
origins = [
    "http://localhost:8080",
]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
import src.router as router
router.rotas(app)


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8080)