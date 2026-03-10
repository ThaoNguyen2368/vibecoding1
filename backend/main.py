from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine, get_db
from models import Student, Base

Base.metadata.create_all(bind=engine)

# Pydantic models
class StudentCreate(BaseModel):
    student_id: str
    name: str
    birth_year: int
    major: str
    gpa: float

class StudentResponse(BaseModel):
    id: int
    student_id: str
    name: str
    birth_year: int
    major: str
    gpa: float
    
    class Config:
        from_attributes = True

# FastAPI app
app = FastAPI(title="Student Management System", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routes
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Student Management System API"}

@app.get("/students", response_model=List[StudentResponse], tags=["Students"])
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students

@app.post("/students", response_model=StudentResponse, tags=["Students"])
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    # Check if student_id already exists
    existing_student = db.query(Student).filter(Student.student_id == student.student_id).first()
    if existing_student:
        raise HTTPException(status_code=400, detail="Student ID already exists")
    
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.put("/students/{student_id}", response_model=StudentResponse, tags=["Students"])
def update_student(student_id: str, student: StudentCreate, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.student_id == student_id).first()
    
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    for key, value in student.dict().items():
        setattr(db_student, key, value)
    
    db.commit()
    db.refresh(db_student)
    return db_student

@app.delete("/students/{student_id}", tags=["Students"])
def delete_student(student_id: str, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.student_id == student_id).first()
    
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db.delete(db_student)
    db.commit()
    return {"message": "Student deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
