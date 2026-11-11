from datetime import date

from pydantic import BaseModel, ConfigDict

class ProjectCreat(BaseModel):
    name:str
    description:str|None=None
  
    
    
class PrjectUpdate(BaseModel):
    name:str|None=None
    description:str|None=None
    
    model_config = ConfigDict(from_attributes=True)
    
    
    
    
class ProjectResponse(BaseModel):
    id:int
    name:str
    description:str|None=None
   
    
    
    model_config = ConfigDict(from_attributes=True)
    
class EmployeeCreat(BaseModel):
    full_name:str
    email:str
    positition:str
    is_active:bool
  
    
class EmployeeUpdate(BaseModel):
    full_name:str|None=None
    email:str|None=None
    positition:str|None=None
    is_active:bool|None=None
    
class EmployeeReponse(BaseModel):
    id:int
    full_name:str
    email:str
    positition:str
    is_active:bool
    
    model_config = ConfigDict(from_attributes=True)
    
class TaskCreat(BaseModel):
    title:str
    description:str|None=None
    status:str
    prioriti:int
    deadline:date
    project_id:int
    employe_id:int            
    
class TaskUpdate(BaseModel):
    title:str|None=None
    description:str|None=None
    status:str|None=None
    prioriti:int|None=None
    deadline:date|None=None
    project_id:int|None=None
    employe_id:int|None=None
    
class TaskAssign(BaseModel):
    employe_id:int


class TaskStatus(BaseModel):
    status:str


class TaskReponse(BaseModel):
    id:int
    title:str
    description:str|None=None
    status:str
    prioriti:int
    deadline:date
    project_id:int
    employe_id:int
    
    model_config = ConfigDict(from_attributes=True)
    
