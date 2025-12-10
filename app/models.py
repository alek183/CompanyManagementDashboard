from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date

#Employee models

class EmployeeBase(BaseModel):
    first_name: str = Field(..., max_length=100)
    last_name: str = Field(..., max_length=100)

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True

#Client models

class ClientBase(BaseModel):
    name: str = Field(..., max_length=100)
    mail: EmailStr
    contact_number: str = Field(..., max_length=100)

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True

#Task models

class TaskBase(BaseModel):
    title: str = Field(..., max_length=100)
    description: Optional[str] = None
    status: str = "Pending"
    employee_id: Optional[int] = None
    client_id: Optional[int] = None
    creation_date: date
    due_date: date

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True


#Stats models

class StatsBase(BaseModel):
    date: date
    total_tasks: int = 0
    pending_tasks: int = 0
    in_progress_tasks: int = 0
    overdue_tasks: int = 0
    completed_tasks: int = 0

class StatsCreate(StatsBase):
    pass

class Stats(StatsBase):
    id: int

    class Config:
        orm_mode = True
