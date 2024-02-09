class Student:
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"Student {self.id}: {self.name}, Grade {self.grade}"

# Example usage:
student1 = Student(1, "Alice", "A")
print(student1)
#The __repr__ method in Python is used to return a string representation of an object. It's typically used for debugging and logging purposes to provide a human-readable representation of an object.