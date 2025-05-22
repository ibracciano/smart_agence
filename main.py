from config.config import connect_db, disconnect_db
from src.routes.agent_router import agent_router
from src.routes.ticket_router import ticket_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn


#version de l'api
version = "v1"

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await connect_db()
        yield
    finally:
        await disconnect_db()

app = FastAPI(
    lifespan=lifespan,
    title="SMART AGENCE API",
    description="Application de Gestion de Clients pour une Agence",
    version=version
)

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.on_event("startup")
# async def startup_event():
#     await connect_db()

# @app.on_event("shutdown")
# async def shutdown_event():
#     await disconnect_db()



#route de test
@app.get(f'/api/{version}')
async def root():
    return {"message" : "Bienvenue sur mon API"}


app.include_router(agent_router, prefix=f'/api/{version}', tags=['agents'])
app.include_router(ticket_router, prefix=f'/api/{version}', tags=['tickets'])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)