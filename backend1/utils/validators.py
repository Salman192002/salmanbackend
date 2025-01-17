class Validators:
    @staticmethod
    def validate_student_data(data):
        required_fields = ['student_id', 'name', 'age', 'grade']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        
        if not isinstance(data['age'], int) or data['age'] < 0:
            raise ValueError("Age must be a positive integer")
        
        if not isinstance(data['grade'], (int, float)) or data['grade'] < 0 or data['grade'] > 100:
            raise ValueError("Grade must be between 0 and 100")
        
        return True