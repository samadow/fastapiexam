from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import *
from app.schemas import *


def create_project(db: Session, project: ProjectCreat):
    new_project = Project(
        name=project.name,
        description=project.description,
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


def get_projects(db: Session):
    return db.query(Project).all()


def get_project(db: Session, project_id: int):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


def update_project(db: Session, project_id: int, project: PrjectUpdate):
    db_project = db.get(Project, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    data = project.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(db_project, key, value)

    db.commit()
    db.refresh(db_project)
    return db_project

def delete_project(db:Session, project_id :int):
    project = db.get(Project,project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(project)
    db.commit()


def get_project_tasks(db: Session, project_id: int):
    project = db.get(Project, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db.query(Task).filter(Task.project_id == project_id).all()

def create_employe(db: Session, employee: EmployeeCreat):
    new_employe = employee(
        full_name=employee.full_name,
        email=employee.email,
        position=employee.positition,
        is_active = employee.is_active
    )
    db.add(new_employe)
    db.commit()
    db.refresh(new_employe)
    return new_employe

def get_employees(db: Session):
    return db.query(Employee).all()



def get_employee(db: Session, employee_id: int):
    employee = db.query(Project).filter(Project.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Project not found")
    return employee

def update_employee(db: Session, employee_id: int, employee: EmployeeUpdate):
    employe = db.get(Employee, employee_id)
    if employe is None:
        raise HTTPException(status_code=404, detail="Project not found")

    data = employee.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(employee, key, value)

    db.commit()
    db.refresh(employee)
    return employee


def delete_employee(db:Session, employee_id :int):
    employe = db.get(Employee,employee_id)
    if employe is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(employe)
    db.commit()

def get_employee_tasks(db: Session, employe_id: int):
    employe = db.get(Employee, employe_id)
    if employe is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db.query(Task).filter(Task.employe_id == employe_id).all()



def create_task(db: Session, task: TaskCreat):
    task_new = Task(**task.model_dump())
    db.add(task_new)
    db.commit()
    db.refresh(task_new)
    return task_new


def get_tasks(db: Session):
    return db.query(Task).all()


def get_task(db: Session, task_id: int):
    task = db.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# PATCH /tasks/{id} - частичное обновление
def update_task(db: Session, task_id: int, task: TaskUpdate):
    db_task = get_task(db, task_id)

    data = task.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(db_task, key, value)

    db.commit()
    db.refresh(db_task)
    return db_task



def delete_task(db: Session, task_id: int):
    db_task = get_task(db, task_id)
    db.delete(db_task)
    db.commit()


def assign_task(db: Session, task_id: int, data: TaskAssign):
    db_task = get_task(db, task_id)

    employee = db.get(Employee, data.employe_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    if not employee.is_active:
        raise HTTPException(status_code=400, detail="Employee is not active")

    db_task.employe_id = data.employe_id
    db.commit()
    db.refresh(db_task)
    return db_task


ALLOWED_STATUSES = {"todo", "in_progress", "done"}


def change_task_status(db: Session, task_id: int, data: TaskStatus):
    db_task = get_task(db, task_id)

    if data.status not in ALLOWED_STATUSES:
        raise HTTPException(status_code=400, detail=f"Status must be one of {sorted(ALLOWED_STATUSES)}")

    db_task.status = data.status
    db.commit()
    db.refresh(db_task)
    return db_task
