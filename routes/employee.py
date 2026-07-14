from fastapi import APIRouter

from services.employee_service import EmployeeService

router = APIRouter()

service = EmployeeService()


@router.get("/employee/version")
def version():

    return {

        "SQLVersion": service.get_sql_version()

    }