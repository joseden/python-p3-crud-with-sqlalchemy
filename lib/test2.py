from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create engine and session
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

# Define declarative base
Base = declarative_base()

# Define Student class
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    grade = Column(String)

# Create tables
Base.metadata.create_all(engine)

# Create a list of Student objects
students = [
    Student(name='Alice', grade='A'),
    Student(name='Bob', grade='B'),
    Student(name='Charlie', grade='C')
]

# Bulk insert students into the database
session.bulk_save_objects(students)

# Commit the session to persist the changes
session.commit()
