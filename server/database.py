import os
import motor.motor_asyncio
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv()

MONGO_DETAILS = os.environ.get("MONGO_DETAILS")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students
student_collection = database.get_collection("students_collection")


def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "gpa": student["gpa"],
    }


# Retrieve all students present in the database
async def retrieve_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students


# Add a new student into to the database
async def add_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


# Retrieve a student with a matching ID
async def retrieve_student(student_id: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(student_id)})
    if student:
        return student_helper(student)


# Update a student with a matching ID
async def update_student(student_id: str, student_data: dict) -> dict:
    student = await student_collection.find_one_and_update(
        {"_id": ObjectId(student_id)},
        {"$set": student_data},
        return_document=True,
    )
    return student_helper(student)


# Delete a student from the database
async def delete_student(student_id: str) -> bool:
    result = await student_collection.delete_one({"_id": ObjectId(student_id)})
    return result.deleted_count > 0
