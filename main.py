from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

origins = [
    "http://group15.exceed19.online",
    "https://group15.exceed19.online",
    "http://group15.exceed19.online:80",
    "https://group15.exceed19.online:80",
    "http://localhost",
    "http://localhost:80",
]

from routers import bulb, party

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(bulb.router)
app.include_router(party.router)


@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )
