import pandas as pd
import os

# Define the path for the data file
DATA_FILE = 'students.csv'

def get_initial_data():
    """Returns a DataFrame with initial synthetic student data."""
    return pd.DataFrame({
        'RegistrationNo': ['S001', 'S002', 'S003', 'S004', 'S005'],
        'Name': ['Aryan Sharma', 'Priya Singh', 'Rohan Mehta', 'Sneha Gupta', 'Vikram Kumar'],
        'Department': ['Computer Science', 'Electronics', 'Mechanical', 'Computer Science', 'Civil'],
        'CRS_Score': [810, 750, 680, 850, 620],
        'Current_CGPA': [8.75, 8.2, 7.9, 9.1, 7.5],
        'Attendance_Percentage': [92, 88, 95, 91, 85],
        'Target_Job_Profile': ['Data Scientist', 'Embedded Systems Engineer', 'Design Engineer', 'Software Engineer', 'Structural Engineer']
    })

def load_data():
    """
    Loads student data from the CSV file.
    If the file doesn't exist, it creates it with initial sample data.
    """
    if not os.path.exists(DATA_FILE):
        print(f"Data file not found. Creating '{DATA_FILE}' with sample data.")
        df = get_initial_data()
        df.to_csv(DATA_FILE, index=False)
        return df
    try:
        return pd.read_csv(DATA_FILE)
    except pd.errors.EmptyDataError:
        print("Data file is empty. Initializing with sample data.")
        df = get_initial_data()
        df.to_csv(DATA_FILE, index=False)
        return df


def save_data(df):
    """Saves the entire DataFrame to the CSV file."""
    try:
        df.to_csv(DATA_FILE, index=False)
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

def add_student(student_data):
    """Adds a new student to the dataset."""
    df = load_data()
    # Check if RegistrationNo already exists
    if student_data['RegistrationNo'] in df['RegistrationNo'].values:
        print(f"Error: Registration number {student_data['RegistrationNo']} already exists.")
        return False, "Registration number already exists."

    new_student_df = pd.DataFrame([student_data])
    df = pd.concat([df, new_student_df], ignore_index=True)
    save_data(df)
    return True, "Student added successfully."

def update_student(reg_no, updated_data):
    """Updates an existing student's data identified by RegistrationNo."""
    df = load_data()
    if reg_no not in df['RegistrationNo'].values:
        return False, "Student not found."

    student_index = df.index[df['RegistrationNo'] == reg_no].tolist()[0]
    for key, value in updated_data.items():
        if key in df.columns:
            df.loc[student_index, key] = value
    save_data(df)
    return True, "Student updated successfully."

def get_student_by_reg_no(reg_no):
    """Retrieves a single student's data by their RegistrationNo."""
    df = load_data()
    student_data = df[df['RegistrationNo'] == reg_no]
    if not student_data.empty:
        return student_data.to_dict('records')[0]
    return None

def student_exists(reg_no):
    """Checks if a student with the given RegistrationNo exists."""
    df = load_data()
    return reg_no in df['RegistrationNo'].values
