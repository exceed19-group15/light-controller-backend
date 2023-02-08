from fastapi import FastAPI

from routers import bulb, party

app = FastAPI()

app.include_router(bulb.router)
app.include_router(party.router)
