from pydantic import BaseModel
from typing import Optional
from datetime import date


class ProfileUpdate(BaseModel):
    student_id: int
    name: Optional[str] = None
    email: Optional[str] = None
    new_password: Optional[str] = None


class AttendanceCreate(BaseModel):
    student_id: int
    date: date
    status: str  # Example: "Present" or "Absent"


class TestCreate(BaseModel):
    teacher_id: int
    student_id: Optional[int] = None
    title: str
    content: str
    score: Optional[float] = None


class TestSubmissionCreate(BaseModel):
    id: int
    student_id: int
    submission_content: str
    score: Optional[float] = None


class FeedbackCreate(BaseModel):
    from_user_id: int
    to_user_id: int
    message: str


class ClassroomAllocationCreate(BaseModel):
    classroom_id: int
    teacher_id: int
    subject: str

class SyllabusProgressCreate(BaseModel):
    class_id: int
    subject: str
    progress: str


class SyllabusUpdate(BaseModel):
    progress: str