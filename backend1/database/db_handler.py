import json
import os
from pathlib import Path

class DatabaseHandler:
    def __init__(self, db_file="database/students.json"):
        self.db_file = db_file
        self._ensure_db_exists()
    
    def _ensure_db_exists(self):
        db_path = Path(self.db_file)
        db_path.parent.mkdir(exist_ok=True)
        if not db_path.exists():
            with open(self.db_file, 'w') as f:
                json.dump([], f)
    
    def read_all(self):
        with open(self.db_file, 'r') as f:
            return json.load(f)
    
    def write_all(self, data):
        with open(self.db_file, 'w') as f:
            json.dump(data, f, indent=4)
    
    def add_student(self, student):
        data = self.read_all()
        data.append(student.to_dict())
        self.write_all(data)
    
    def get_student(self, student_id):
        data = self.read_all()
        for student_data in data:
            if student_data['student_id'] == student_id:
                return student_data
        return None
    
    def update_student(self, student_id, updated_data):
        data = self.read_all()
        for i, student in enumerate(data):
            if student['student_id'] == student_id:
                data[i].update(updated_data)
                self.write_all(data)
                return True
        return False
    
    def delete_student(self, student_id):
        data = self.read_all()
        initial_length = len(data)
        data = [s for s in data if s['student_id'] != student_id]
        if len(data) < initial_length:
            self.write_all(data)
            return True
        return False