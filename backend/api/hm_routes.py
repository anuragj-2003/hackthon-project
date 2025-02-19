# /home/lenovo/Videos/hackathon-project/backend/api/hm_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import FeedbackCreate, ClassroomAllocationCreate
from models import Feedback, ClassroomAllocation


router = APIRouter(prefix="/hm", tags=["HM"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/feedback")
def add_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    db_feedback = Feedback(
        from_user_id=feedback.from_user_id,
        to_user_id=feedback.to_user_id,
        message=feedback.message
    )
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback


@router.post("/classroom")
def allocate_classroom(allocation: ClassroomAllocationCreate, db: Session = Depends(get_db)):
    db_allocation = ClassroomAllocation(
        teacher_id=allocation.teacher_id,
        classroom_number=allocation.classroom_number,
        time_slot=allocation.time_slot
    )
    db.add(db_allocation)
    db.commit()
    db.refresh(db_allocation)
    return db_allocation
