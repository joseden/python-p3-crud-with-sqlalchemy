#!/usr/bin/env python3

from datetime import datetime

from sqlalchemy import (create_engine, desc, func,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    Index('index_name', 'name')

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())
    
    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.name}, " \
            + f"Grade {self.grade}"

    
if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    
     # use our engine to configure a 'Session' class
    Session = sessionmaker(bind=engine)
    # use 'Session' class to create 'session' object
    session = Session()
    
    Session = sessionmaker(bind=engine)
    session = Session()

    albert_einstein = Student(
        name="Albert Einstein",
        email="albert.einstein@zurich.edu",
        grade=6,
        birthday=datetime(
            year=1879,
            month=3,
            day=14
        ),
    )
    
    alan_turing = Student(
        name="Alan Turing",
        email="alan.turing@sherborne.edu",
        grade=11,
        birthday=datetime(
            year=1912,
            month=6,
            day=23
        ),
    )

    session.bulk_save_objects([albert_einstein,alan_turing])
    session.commit()
    
    students = session.query(Student).all()
    
    names = session.query(Student.name).all()
    
    students_by_name = session.query(
            Student.name).order_by(
            Student.name).all()
            
    students_by_grade_desc = session.query(
            Student.name, Student.grade).order_by(
            desc(Student.grade)).all()
    
    oldest_student = session.query(
            Student.name, Student.birthday).order_by(
            Student.birthday).limit(1).all()
    
    oldest_student = session.query(
            Student.name, Student.birthday).order_by(
            Student.birthday).first()
    
    student_count = session.query(func.count(Student.id)).first()
    
    query = session.query(Student).filter(Student.name.like('%Alan%'),
        Student.grade == 11).all()

    for record in query:
        print(record.name)
        
         
    for student in session.query(Student):
        student.grade += 1

    session.commit()

    print([(student.name,
        student.grade) for student in session.query(Student)])
    
    
    #update()
    session.query(Student).update({
        Student.grade: Student.grade + 1
    })

    print([(
        student.name,
        student.grade
    ) for student in session.query(Student)])
    
    #delete()
    query = session.query(
        Student).filter(
            Student.name == "Albert Einstein")

    # retrieve first matching record as object
    albert_einstein = query.first()

    # delete record
    session.delete(albert_einstein)
    session.commit()

    # try to retrieve deleted record
    albert_einstein = query.first()

   
   
    print(student_count)

    print(oldest_student)
    print(oldest_student)
    
    print(students_by_grade_desc)
    
    print(students_by_name)
    
    print(names)
    
    print([student for student in students]) #list comprehension
    print(students)
    
    print(albert_einstein)

    


    

