class Student:
    id = 113
    cgpa = 3.91
    name = 'Ira'

    def __str__(self):
        return f"Student(id={self.id}, cgpa={self.cgpa}, name='{self.name}')"

s1 = Student()
print(s1)         # Outputs a user-friendly string representation
print(s1.name)    # Outputs: Mahmud
