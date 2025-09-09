import pandas as pd 
import numpy as np 

filepath = '/Users/thananpornsethjinda/Desktop/internship/projects/in-progress/student-performance-classification/data/raw.csv'

df = pd.read_csv(filepath)


def columnMapping(df: pd.DataFrame) -> pd.DataFrame: # the intermediate data 

    column_info = {
    'STUDENT ID':'id',
    '1': 'student_age',
    '2': 'sex',
    '3': 'high_school_type',
    '4': 'scholarship_type',
    '5': 'additional_work',
    '6': 'artistic_sports_activity',
    '7': 'has_partner',
    '8': 'salary',
    '9': 'transportation',
    '10': 'accommodation_type',
    '11': 'mother_education',
    '12': 'father_education',
    '13': 'siblings',
    '14': 'parental_status',
    '15': 'mother_occupation',
    '16': 'father_occupation',
    '17': 'weekly_study_hours',
    '18': 'reading_freq_non_sci',
    '19': 'reading_freq_sci',
    '20': 'seminar_attendance',
    '21': 'project_impact',
    '22': 'class_attendance',
    '23': 'prep_midterm_1',
    '24': 'prep_midterm_2',
    '25': 'note_taking',
    '26': 'listening_in_class',
    '27': 'discussion_interest',
    '28': 'flip_classroom',
    '29': 'last_semester_gpa',
    '30': 'expected_gpa',
    'COURSE ID': 'course_id',
    'GRADE': 'output_grade'
    }

    df = df.copy()

    df.columns = df.columns.map(column_info)

    return df 

def valueMapping(df: pd.DataFrame) -> pd.DataFrame:    

    mappings = {
        'sex': {1:'female', 2:'male'},
        'has_partner': {1:'yes', 2:'no'},
        'parental_status': {1:'married', 2:'divorced', 3:'died'},
        'high_school_type': {1:'private', 2:'state', 3:'other'},
        'additional_work': {1:'yes', 2:'no'},
        'artistic_sports_activity': {1:'yes', 2:'no'},
        'mother_occupation': {1:'retired', 2:'housewife', 3:'government officer', 
                            4:'private sector employee', 5:'self-employment', 6:'other'},
        'father_occupation': {1:'retired', 2:'government officer', 3:'private sector employee', 
                            4:'self-employment', 5:'other'},
        'transportation': {1:'bus', 2:'private car/taxi', 3:'bicycle', 4:'other'},
        'accommodation_type': {1:'rental', 2:'dormitory', 3:'with_family', 4:'other'},
        'seminar_attendance' : {1: 'yes', 2: 'no'},
        'flip_classroom' : {1: 'not_useful', 2: 'useful', 3: 'not_applicable'},
        'prep_midterm_1' : {1: 'alone', 2: 'with_friends', 3: 'not_applicable'},
        'prep_midterm_2' : {1: 'close', 2: 'regular', 3: 'never'},
        'class_attendance' : {1: 3, 2:2, 3:1},
        'project_impact' : {1:3, 2:1, 3:2}
    }
    
    for column, mapping in mappings.items():
        df[column] = df[column].map(mapping)
        
    return df

# def preprocessing(df: pd.DataFrame) -> pd.DataFrame: 

#     df = df.copy()

#     intermediate_df = columnMapping(df)

#     final_df = valueMapping(intermediate_df)

    # Preprocessing steps 


