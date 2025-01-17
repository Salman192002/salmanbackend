class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
    
    def to_dict(self):
        return {
            'student_id': self.student_id,
            'name': self.name,
            'age': self.age,
            'grade': self.grade
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data['student_id'],
            data['name'],
            data['age'],
            data['grade']
        )
