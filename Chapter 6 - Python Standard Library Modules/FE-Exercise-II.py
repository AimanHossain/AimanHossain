import json

def read_and_display_json():
    
    json_file_path = "C:\\Users\\ibrah\\Documents\\GitHub\\AimanHossain\\Chapter 6 - Python Standard Library Modules\\students.json"


    try:
        with open(json_file_path, "r") as file:
            students_data = json.load(file)

        print("Student Details:")
        for student in students_data:
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grade: {student['grade']}")
            print(f"City: {student['city']}")
            print()

    except FileNotFoundError:
        print(f"The file '{json_file_path}' does not exist.")

if __name__ == "__main__":
    read_and_display_json()
