from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.db import get_db
from app.schemas import TaskCreat, TaskUpdate, TaskReponse, TaskAssign, TaskStatus

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

DB = Annotated[Session, Depends(get_db)]


@router.post("/", response_model=TaskReponse)
def create_task(task: TaskCreat, db: DB):
    return crud.create_task(db, task)


@router.get("/", response_model=list[TaskReponse])
def get_tasks(db: DB):
    return crud.get_tasks(db)


@router.get("/{task_id}", response_model=TaskReponse)
def get_task(task_id: int, db: DB):
    return crud.get_task(db, task_id)


@router.patch("/{task_id}", response_model=TaskReponse)
def update_task(task_id: int, task: TaskUpdate, db: DB):
    return crud.update_task(db, task_id, task)


@router.delete("/{task_id}")
def delete_task(task_id: int, db: DB):
    crud.delete_task(db, task_id)
    return {"detail": "Task deleted"}


@router.patch("/{task_id}/assign", response_model=TaskReponse)
def assign_task(task_id: int, data: TaskAssign, db: DB):
    return crud.assign_task(db, task_id, data)


@router.patch("/{task_id}/status", response_model=TaskReponse)
def change_task_status(task_id: int, data: TaskStatus, db: DB):
    return crud.change_task_status(db, task_id, data)
