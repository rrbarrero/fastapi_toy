from fastapi import FastAPI
from buko.server.routes.student import router as student_router
from buko.server.routes.user import router as user_router

app = FastAPI()


app.include_router(student_router, tags=["Student"], prefix="/student")
app.include_router(user_router, tags=["User"], prefix="/user")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome!"}
