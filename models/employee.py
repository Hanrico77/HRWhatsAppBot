from pydantic import BaseModel
from typing import Optional


class Employee(BaseModel):
    emp_no: str
    name: str
    surname: str
    job_title: Optional[str] = None
    department: Optional[str] = None
    email: Optional[str] = None