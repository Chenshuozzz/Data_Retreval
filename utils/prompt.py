def get_schema(db_id):
    return  '''
    PRAGMA foreign_keys = ON;
    CREATE TABLE `Course_Authors_and_Tutors` (
    `author_id` INTEGER PRIMARY KEY,
    `author_tutor_ATB` VARCHAR(3),
    `login_name` VARCHAR(40),
    `password` VARCHAR(40),
    `personal_name` VARCHAR(80),
    `middle_name` VARCHAR(80),
    `family_name` VARCHAR(80),
    `gender_mf` VARCHAR(1),
    `address_line_1` VARCHAR(80)
    );
    CREATE TABLE `Students` (
    `student_id` INTEGER PRIMARY KEY,
    `date_of_registration` DATETIME,
    `date_of_latest_logon` DATETIME,
    `login_name` VARCHAR(40),
    `password` VARCHAR(10),
    `personal_name` VARCHAR(40),
    `middle_name` VARCHAR(40),
    `family_name` VARCHAR(40)
    );
    CREATE TABLE `Courses` (
    `course_id` INTEGER PRIMARY KEY,
    `author_id` INTEGER NOT NULL,
    `course_name` VARCHAR(120),
    `course_description` VARCHAR(255),
    FOREIGN KEY (`author_id` ) REFERENCES `Course_Authors_and_Tutors`(`author_id` )
    );
    CREATE TABLE `Student_Course_Enrolment` (
    `registration_id` INTEGER PRIMARY KEY,
    `student_id` INTEGER NOT NULL,
    `course_id` INTEGER NOT NULL,
    `date_of_enrolment` DATETIME NOT NULL,
    `date_of_completion` DATETIME NOT NULL,
    FOREIGN KEY (`course_id` ) REFERENCES `Courses`(`course_id` ),
    FOREIGN KEY (`student_id` ) REFERENCES `Students`(`student_id` )
    );
    CREATE TABLE `Student_Tests_Taken` (
    `registration_id` INTEGER NOT NULL,
    `date_test_taken` DATETIME NOT NULL,
    `score` INTEGER NOT NULL,
    FOREIGN KEY (`registration_id` ) REFERENCES `Student_Course_Enrolment`(`registration_id` )
    );'''

def get_nlq():
    return "Analyze this year's English course scores."

def get_prompt():
    task_desc = "You will be provided with a database schema and a problem related to it. Your task involes collect data, generate a report no less than 500 words to solve the prolem. Let's first understand the problem and devise a multi-step plan. Finally, you shold gather the data and generation report.\nRemember:\n(1)Reason the problem step by step.\n(2)Be sure these queries to be valid.\n(3)Deliver every step in this format:Step 1: ['Action': What data you want, 'thought': why you need it, 'query': the relevant query ......]\n(4)Do NOT make up data and I will give you the result of the query.\n(5)Every step can only be completed with one query.\n(6)Get the most out of your data to generate a logical, detailed, coherent reports. \nLet's Begin!\n"


#     task_desc = '''You are an AI trained in analyzing data and generating reports.You will be provided with a database schema and a problem related to it. Your task involes collect data, generate a report no less than 500 words to solve the prolem. Let's first understand the problem and devise a complete plan Finally, you shold gather the data and generation report.
# Remember:
# (1)Reason problem step by step.
# (2)Be sure these queries are valid.
# (3)Deliver your plan in this format:[Step 1: 'Action': What data you want, 'thought': why you need it, 'query': the query to be excuted, 'result': result of the query. Step 2: 'Action': What data you want, 'thought': why you need it, 'query': the query to be excuted. 'result': result of the query.Step 3: ......]
# (4)Every step can only be completed with one query.
# (5)After generating a step you need to wait for me to give you the data from the query you gave me, after I give you the data you can generate the next step. 
# (6)When generating a report you need to be careful to analyze the data I give you.
# Let's Begin!
# '''
    schema = get_schema(0)
    nlq = get_nlq()
    prompt = f"{task_desc}schema:{schema}\nnlq:{nlq}\nstep 1:"

    return prompt

    

if __name__ == "__main__":
    get_prompt()