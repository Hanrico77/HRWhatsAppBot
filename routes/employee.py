from fastapi import APIRouter, HTTPException

from services.employee_service import EmployeeService

router = APIRouter()

service = EmployeeService()


@router.get("/employee/{emp_no}")
async def get_employee(emp_no: str):

    employee = service.get_employee(emp_no)

    if employee is None:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee

@router.get("/employee/search/{search_text}")
async def search_employee(search_text: str):

    return service.search_employee(search_text)