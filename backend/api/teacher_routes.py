# /home/lenovo/Videos/hackathon-project/backend/api/teacher_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import AttendanceCreate, SyllabusProgressCreate, SyllabusUpdate, TestCreate
from models import Attendance, SyllabusProgress, TestAssignment, User


router = APIRouter(prefix="/teacher", tags=["Teacher"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/attendance")
def add_student_attendance(attendance: AttendanceCreate, db: Session = Depends(get_db)):
    student = db.query(User).filter(User.id == attendance.student_id, User.role == "Student").first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db_attendance = Attendance(
        user_id=attendance.student_id,
        date=attendance.date,
        status=attendance.status
    )
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance


@router.post("/syllabus_progress")
def create_syllabus_progress(progress: SyllabusProgressCreate, db: Session = Depends(get_db)):
    teacher = db.query(User).filter(User.id == progress.teacher_id, User.role == "Teacher").first()
    student = db.query(User).filter(User.id == progress.student_id, User.role == "Student").first()

    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db_progress = SyllabusProgress(
        teacher_id=progress.teacher_id,
        student_id=progress.student_id,
        progress_percent=progress.progress_percent
    )
    db.add(db_progress)
    db.commit()
    db.refresh(db_progress)
    return db_progress


@router.put("/syllabus_progress/{progress_id}")
def update_syllabus_progress(progress_id: int, update: SyllabusUpdate, db: Session = Depends(get_db)):
    syllabus_progress = db.query(SyllabusProgress).filter(SyllabusProgress.id == progress_id).first()
    if not syllabus_progress:
        raise HTTPException(status_code=404, detail="Syllabus Progress Record not found")

    syllabus_progress.progress_percent = float(update.progress)

    db.commit()
    db.refresh(syllabus_progress)
    return {"message": "Syllabus progress updated successfully", "progress": syllabus_progress}


@router.post("/test")
def create_test(test: TestCreate, db: Session = Depends(get_db)):
    teacher = db.query(User).filter(User.id == test.teacher_id, User.role == "Teacher").first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    if test.student_id:
        student = db.query(User).filter(User.id == test.student_id, User.role == "Student").first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

    db_test = TestAssignment(
        teacher_id=test.teacher_id,
        student_id=test.student_id,
        title=test.title,
        content=test.content,
        score=test.score
    )
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test


@router.get("/attendance/{student_id}")
def view_student_attendance(student_id: int, db: Session = Depends(get_db)):
    attendance_records = db.query(Attendance).filter(Attendance.user_id == student_id).all()
    if not attendance_records:
        raise HTTPException(status_code=404, detail="No attendance records found for this student")
    return attendance_records


@router.get("/marks/{student_id}")
def track_student_marks(student_id: int, db: Session = Depends(get_db)):
    marks_records = db.query(TestAssignment).filter(TestAssignment.student_id == student_id).all()
    if not marks_records:
        raise HTTPException(status_code=404, detail="No marks records found for this student")
    return marks_records
