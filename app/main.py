from fastapi import FastAPI


from app.db import Base, engine
from app.routers import project, task


Base.metadata.create_all(bind=engine)

app = FastAPI(title='saidjafar')

app.include_router(project.router)
app.include_router(task.router)
