from main import StudentManagementSystem

if __name__ == "__main__":
    sms = StudentManagementSystem()
    
    # Add a new student
    success, message = sms.add_student({
        'student_id': '001',
        'name': 'John Doe',
        'age': 20,
        'grade': 85.5
    })
    print(f"Adding student: {message}")
    
    # Get student details
    success, student = sms.get_student('001')
    if success:
        print(f"Student found: {student.name}")
    
    # Update student
    success, message = sms.update_student('001', {'grade': 90.0})
    print(f"Updating student: {message}")
    
    # List all students
    students = sms.list_all_students()
    print(f"Total students: {len(students)}")