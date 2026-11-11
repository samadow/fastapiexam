from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.db import get_db
from app.schemas import ProjectCreat, PrjectUpdate, ProjectResponse, TaskReponse

router = APIRouter(
    prefix="/project",
    tags=["Project"],
)

DB = Annotated[Session, Depends(get_db)]


@router.post("/create_project", response_model=ProjectResponse)
def create_project(project: ProjectCreat, db: DB):
    return crud.create_project(db, project)


@router.get("/get_projects", response_model=list[ProjectResponse])
def get_projects(db: DB):
    return crud.get_projects(db)


@router.get("/get_project_id/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int, db: DB):
    return crud.get_project(db, project_id)


@router.patch("/update-project/{project_id}", response_model=ProjectResponse)
def update_project(project_id: int, project: PrjectUpdate, db: DB):
    return crud.update_project(db, project_id, project)


@router.get("/{project_id}/tasks", response_model=list[TaskReponse])
def get_project_tasks(project_id: int, db: DB):
    return crud.get_project_tasks(db, project_id)


@router.delete("/delete-project/{project_id}")
def delete_project(project_id: int, db: DB):
    crud.delete_project(db, project_id)
    return {"detail": "Project deleted"}
