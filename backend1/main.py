from models.student import Student
from database.db_handler import DatabaseHandler
from utils.validators import Validators

class StudentManagementSystem:
    def __init__(self):
        self.db = DatabaseHandler()
    
    def add_student(self, student_data):
        try:
            Validators.validate_student_data(student_data)
            student = Student(**student_data)
            self.db.add_student(student)
            return True, "Student added successfully"
        except ValueError as e:
            return False, str(e)
    
    def get_student(self, student_id):
        student_data = self.db.get_student(student_id)
        if student_data:
            return True, Student.from_dict(student_data)
        return False, "Student not found"
    
    def update_student(self, student_id, updated_data):
        try:
            if 'student_id' in updated_data:
                del updated_data['student_id']  # Prevent ID modification
            
            current_data = self.db.get_student(student_id)
            if not current_data:
                return False, "Student not found"
            
            merged_data = {**current_data, **updated_data}
            Validators.validate_student_data(merged_data)
            
            success = self.db.update_student(student_id, updated_data)
            return (True, "Student updated successfully") if success else (False, "Update failed")
        except ValueError as e:
            return False, str(e)
    
    def delete_student(self, student_id):
        success = self.db.delete_student(student_id)
        return (True, "Student deleted successfully") if success else (False, "Student not found")
    
    def list_all_students(self):
        students_data = self.db.read_all()
        return [Student.from_dict(data) for data in students_data]
