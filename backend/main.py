from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from typing import List, Optional
import csv
import io
import os

from database import SessionLocal, engine, get_db
from models import Student, Class, Base

Base.metadata.create_all(bind=engine)

# CSV Import Functions
def import_students_from_csv(db: Session):
    csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'student.csv')
    if os.path.exists(csv_path):
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            students_data = list(reader)
            for row in students_data:
                # Check if student already exists
                existing_student = db.query(Student).filter(Student.student_id == row['student_id']).first()
                if not existing_student:
                    student = Student(
                        student_id=row['student_id'],
                        name=row['name'],
                        birth_year=int(row['birth_year']),
                        major=row['major'],
                        gpa=float(row['gpa'])
                    )
                    db.add(student)
            db.commit()
            print(f"Imported {len(students_data)} students from CSV")

def import_classes_from_csv(db: Session):
    csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'class.csv')
    if os.path.exists(csv_path):
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            classes_data = list(reader)
            for row in classes_data:
                # Check if class already exists
                existing_class = db.query(Class).filter(Class.class_id == row['class_id']).first()
                if not existing_class:
                    cls = Class(
                        class_id=row['class_id'],
                        class_name=row['class_name'],
                        advisor=row['advisor']
                    )
                    db.add(cls)
            db.commit()
            print(f"Imported {len(classes_data)} classes from CSV")

# Auto-import CSV data on startup
def initialize_data():
    db = SessionLocal()
    try:
        import_classes_from_csv(db)
        import_students_from_csv(db)
    finally:
        db.close()

# Initialize data when app starts
initialize_data()

# Pydantic models
class ClassCreate(BaseModel):
    class_id: str
    class_name: str
    advisor: str

class ClassResponse(BaseModel):
    id: int
    class_id: str
    class_name: str
    advisor: str
    
    class Config:
        from_attributes = True

class StudentCreate(BaseModel):
    student_id: str
    name: str
    birth_year: int
    major: str
    gpa: float
    class_id: Optional[str] = None

class StudentResponse(BaseModel):
    id: int
    student_id: str
    name: str
    birth_year: int
    major: str
    gpa: float
    class_id: Optional[str] = None
    class_info: Optional[ClassResponse] = None
    
    class Config:
        from_attributes = True

class Statistics(BaseModel):
    total_students: int
    average_gpa: float
    students_by_major: dict

# FastAPI app
app = FastAPI(title="Student Management System", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_cors_headers(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

# API Routes
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Student Management System API"}

# Class endpoints
@app.get("/classes", response_model=List[ClassResponse], tags=["Classes"])
def get_classes(db: Session = Depends(get_db)):
    classes = db.query(Class).all()
    return classes

@app.post("/classes/import", tags=["Classes"])
def import_classes(db: Session = Depends(get_db)):
    try:
        import_classes_from_csv(db)
        return {"message": "Classes imported successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error importing classes: {str(e)}")

@app.post("/classes", response_model=ClassResponse, tags=["Classes"])
def create_class(class_data: ClassCreate, db: Session = Depends(get_db)):
    # Check if class_id already exists
    existing_class = db.query(Class).filter(Class.class_id == class_data.class_id).first()
    if existing_class:
        raise HTTPException(status_code=400, detail="Class ID already exists")
    
    db_class = Class(**class_data.dict())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

@app.put("/classes/{class_id}", response_model=ClassResponse, tags=["Classes"])
def update_class(class_id: str, class_data: ClassCreate, db: Session = Depends(get_db)):
    db_class = db.query(Class).filter(Class.class_id == class_id).first()
    
    if not db_class:
        raise HTTPException(status_code=404, detail="Class not found")
    
    for key, value in class_data.dict().items():
        setattr(db_class, key, value)
    
    db.commit()
    db.refresh(db_class)
    return db_class

@app.delete("/classes/{class_id}", tags=["Classes"])
def delete_class(class_id: str, db: Session = Depends(get_db)):
    db_class = db.query(Class).filter(Class.class_id == class_id).first()
    
    if not db_class:
        raise HTTPException(status_code=404, detail="Class not found")
    
    db.delete(db_class)
    db.commit()
    return {"message": "Class deleted successfully"}

# Student endpoints
@app.get("/students", response_model=List[StudentResponse], tags=["Students"])
def get_students(db: Session = Depends(get_db)):
    from sqlalchemy.orm import joinedload
    students = db.query(Student).options(joinedload(Student.class_info)).all()
    return students

@app.get("/students/search", response_model=List[StudentResponse], tags=["Students"])
def search_students(name: str, db: Session = Depends(get_db)):
    from sqlalchemy.orm import joinedload
    students = db.query(Student).options(joinedload(Student.class_info)).filter(
        Student.name.ilike(f"%{name}%")
    ).all()
    return students

@app.post("/students/import", tags=["Students"])
def import_students(db: Session = Depends(get_db)):
    try:
        import_students_from_csv(db)
        return {"message": "Students imported successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error importing students: {str(e)}")

@app.post("/students", response_model=StudentResponse, tags=["Students"])
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    # Check if student_id already exists
    existing_student = db.query(Student).filter(Student.student_id == student.student_id).first()
    if existing_student:
        raise HTTPException(status_code=400, detail="Student ID already exists")
    
    # Validate class_id if provided
    if student.class_id:
        class_exists = db.query(Class).filter(Class.class_id == student.class_id).first()
        if not class_exists:
            raise HTTPException(status_code=400, detail="Class ID does not exist")
    
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
    
    # Validate class_id if provided
    if student.class_id:
        class_exists = db.query(Class).filter(Class.class_id == student.class_id).first()
        if not class_exists:
            raise HTTPException(status_code=400, detail="Class ID does not exist")
    
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

# Statistics endpoint
@app.get("/statistics", response_model=Statistics, tags=["Statistics"])
def get_statistics(db: Session = Depends(get_db)):
    total_students = db.query(Student).count()
    
    avg_gpa_result = db.query(func.avg(Student.gpa)).scalar()
    average_gpa = round(float(avg_gpa_result), 2) if avg_gpa_result else 0.0
    
    students_by_major = db.query(
        Student.major, 
        func.count(Student.id).label('count')
    ).group_by(Student.major).all()
    
    major_dict = {major: count for major, count in students_by_major}
    
    return Statistics(
        total_students=total_students,
        average_gpa=average_gpa,
        students_by_major=major_dict
    )

# CSV Export endpoint
@app.get("/export/csv", tags=["Export"])
def export_csv(db: Session = Depends(get_db)):
    from sqlalchemy.orm import joinedload
    students = db.query(Student).options(joinedload(Student.class_info)).all()
    
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['student_id', 'name', 'major', 'gpa', 'class_name'])
    
    # Write data
    for student in students:
        class_name = student.class_info.class_name if student.class_info else ''
        writer.writerow([
            student.student_id,
            student.name,
            student.major,
            student.gpa,
            class_name
        ])
    
    output.seek(0)
    
    return StreamingResponse(
        io.BytesIO(output.getvalue().encode('utf-8')),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=students.csv"}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
