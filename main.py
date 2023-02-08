from fastapi import FastAPI
from starlette.responses import JSONResponse

from routers import bulb, party

app = FastAPI()

app.include_router(bulb.router)
app.include_router(party.router)


@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )
