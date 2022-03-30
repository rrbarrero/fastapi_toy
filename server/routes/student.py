from buko.server.database import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
)
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.models.student import ErrorResponseModel, ResponseModel, StudenSchema

router = APIRouter()


@router.post("/", response_description="Student created")
async def create_student(student: StudenSchema = Body(...)):
    student_data = jsonable_encoder(student)
    new_student = await add_student(student_data)
    return ResponseModel(new_student, "Student added successfully")


@router.get("/", response_description="List of students")
async def get_students():
    students = await retrieve_students()
    return ResponseModel(students, "List of students")


@router.get("/{student_id}", response_description="Student retrieved")
async def get_student(student_id: str):
    student = await retrieve_student(student_id)
    if student:
        return ResponseModel(student, "Student retrieved")
    return ErrorResponseModel("An error ocurred", 404, "Student not found")


@router.put("/{student_id}", response_description="Student updated")
async def update_student_data(student_id: str, UpdateStudentModel=Body(...)):
    student_data = jsonable_encoder(UpdateStudentModel)
    updated_student = await update_student(student_id, student_data)
    if updated_student:
        return ResponseModel(updated_student, "Student updated")
    return ErrorResponseModel("An error ocurred", 404, "Student not found")


@router.delete("/{student_id}", response_description="Student deleted")
async def delete_student_data(student_id: str):
    deleted_student = await delete_student(student_id)
    if deleted_student:
        return ResponseModel(deleted_student, "Student deleted")
    return ErrorResponseModel("An error ocurred", 404, "Student not found")
