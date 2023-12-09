from crud.user import router as crud_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="IvanFitness")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешает все источники
    allow_credentials=True,
    allow_methods=["*"],  # Разрешает все методы
    allow_headers=["*"],  # Разрешает все заголовки
)


@app.get("/users")
async def welcome() -> dict:
    return {
            "message": "Hello World"
            }
app.include_router(crud_router)


