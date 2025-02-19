# /home/lenovo/Videos/hackathon-project/backend/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, Float
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(String)  # HM, Teacher, Student

    feedbacks_given = relationship('Feedback', foreign_keys='Feedback.from_user_id', back_populates='from_user')
    feedbacks_received = relationship('Feedback', foreign_keys='Feedback.to_user_id', back_populates='to_user')
    attendances = relationship('Attendance', back_populates='student')
    tests = relationship('TestAssignment', back_populates='student')


class Attendance(Base):
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Date)
    status = Column(String)  # Present / Absent

    student = relationship('User', back_populates='attendances')


class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True, index=True)
    from_user_id = Column(Integer, ForeignKey('users.id'))
    to_user_id = Column(Integer, ForeignKey('users.id'))
    message = Column(Text)

    from_user = relationship('User', foreign_keys=[from_user_id], back_populates='feedbacks_given')
    to_user = relationship('User', foreign_keys=[to_user_id], back_populates='feedbacks_received')


class TestAssignment(Base):
    __tablename__ = 'test_assignment'

    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey('users.id'))
    student_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    content = Column(Text)
    score = Column(Float)

    teacher = relationship('User', foreign_keys=[teacher_id])
    student = relationship('User', foreign_keys=[student_id], back_populates='tests')



class ClassroomAllocation(Base):
    __tablename__ = 'classroom_allocations'

    id = Column(Integer, primary_key=True, index=True)
    classroom_id = Column(Integer, nullable=False)
    teacher_id = Column(Integer, nullable=False)
    subject = Column(String, nullable=False)

class SyllabusProgress(Base):
    __tablename__ = 'syllabus_progress'

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, nullable=False)
    subject = Column(String, nullable=False)
    progress = Column(String, nullable=False)
