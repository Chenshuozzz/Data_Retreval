## v1:baseline
You will be provided with a database schema and a problem related to it. Your task involes collect data, generate a report no less than 500 words to solve the prolem. Let's first understand the problem and devise a complete plan. Finally, you shold gather the data and generation report.  
Remember:  
(1)Reason problem step by step.  
(2)Be sure these queries are valid.  
(3)Deliver your plan in this format:[Step 1: 'Action': What data you want, 'thought': why you need it, 'query': the query to be excuted, 'result': result of the query. Step 2: 'Action': What data you want, 'thought': why you need it, 'query': the query to be excuted. 'result': result of the query.Step 3: ......]  
(4)Every step can only be completed with one query.  
(5)Stop in every step, and I will give you the result.  
Let's Begin!  
schema：  
question：  
Step 1:


## v2:collect more data
You will be provided with a database schema and a problem related to it. Your task involes collect data, generate a report no less than 500 words to solve the prolem. Let's first understand the problem and devise a complete plan with natural language. Then, decompose the plan into multiple steps. Caryy out the plan by SQL query step by step. Finally, you shold gather the data and generation report.  
Remember:  
(1)Reason the problem step by step.  
(2)Be sure these queries to be valid.  
(3)Deliver every step in this format:Step 1: ['Action': What data you want, 'thought': why you need it ......]  
(4)Stop in every step, and I will give you the result.  
(5)Collect as much data as possible.  
(5)Get the most out of your data to generate a logical, detailed, coherent reports.  
Let's Begin!  
schema：  
question：  
Plan:


## v3:first show all the plan then carry out every step


## schema and question
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
FOREIGN KEY (`author_id` ) REFERENCES `Course_Authors_and_Tutors`(`author_id` ),
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
);

Analyze this year’s English course scores.