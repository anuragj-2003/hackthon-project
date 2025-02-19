# /home/lenovo/Videos/hackathon-project/backend/api/student_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import FeedbackCreate, TestSubmissionCreate, ProfileUpdate
from models import Feedback, TestAssignment, User, Attendance


router = APIRouter(prefix="/student", tags=["Student"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/feedback")
def add_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    from_user = db.query(User).filter(User.id == feedback.from_user_id).first()
    to_user = db.query(User).filter(User.id == feedback.to_user_id).first()

    if not from_user:
        raise HTTPException(status_code=404, detail="Sender (from_user_id) not found")
    if not to_user:
        raise HTTPException(status_code=404, detail="Recipient (to_user_id) not found")

    db_feedback = Feedback(
        from_user_id=feedback.from_user_id,
        to_user_id=feedback.to_user_id,
        message=feedback.message
    )
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback


@router.post("/test_submission")
def submit_test(submission: TestSubmissionCreate, db: Session = Depends(get_db)):
    test_assignment = db.query(TestAssignment).filter(TestAssignment.id == submission.test_assignment_id).first()
    student = db.query(User).filter(User.id == submission.student_id, User.role == "Student").first()

    if not test_assignment:
        raise HTTPException(status_code=404, detail="Test assignment not found")
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Assuming the `TestAssignment` model represents a student's assignment with score updates
    test_assignment.content = submission.submission_content
    test_assignment.score = submission.score

    db.commit()
    db.refresh(test_assignment)
    return {"message": "Test submitted successfully", "test_assignment": test_assignment}


@router.put("/profile/{student_id}")
def update_profile(student_id: int, profile: ProfileUpdate, db: Session = Depends(get_db)):
    student = db.query(User).filter(User.id == student_id, User.role == "Student").first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    if profile.name:
        student.name = profile.name
    if profile.email:
        student.email = profile.email

    db.commit()
    db.refresh(student)
    return {"message": "Profile updated successfully", "student": student}


@router.get("/attendance/{student_id}")
def view_attendance(student_id: int, db: Session = Depends(get_db)):
    attendance_records = db.query(Attendance).filter(Attendance.user_id == student_id).all()

    if not attendance_records:
        raise HTTPException(status_code=404, detail="Attendance records not found for this student")

    return attendance_records


@router.get("/marks/{student_id}")
def view_marks(student_id: int, db: Session = Depends(get_db)):
    marks_records = db.query(TestAssignment).filter(TestAssignment.student_id == student_id).all()

    if not marks_records:
        raise HTTPException(status_code=404, detail="Marks records not found for this student")

    return marks_records
