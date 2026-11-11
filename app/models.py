from sqlalchemy import Column, Integer, String, DateTime, Text, Date, Boolean, ForeignKey, func

from app.db import Base


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, unique=True)
    cr_at = Column(DateTime, server_default=func.now())


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True)
    positition = Column(String(100))
    is_active = Column(Boolean, default=True)
    cr_at = Column(DateTime, server_default=func.now())


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    status = Column(String(20), default="todo")
    prioriti = Column(Integer)
    deadline = Column(Date, nullable=False)
    cr_at = Column(DateTime, server_default=func.now())
    project_id = Column(Integer, ForeignKey("project.id"))
    employe_id = Column(Integer, ForeignKey("employee.id"))
