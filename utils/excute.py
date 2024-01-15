import sqlite3

def execute(db_path, query):
    if '.sqlite' in db_path:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        conn.close()
        column_names = ' '.join(str(x) for x in column_names)
        results = ' '.join(str(x) for x in results)
        return column_names, results

if __name__ == "__main__":
    db_path = '../database/db.sqlite'
    query = 'select course_id, course_name from Courses'
    column_names, results = execute(db_path, query)
    print(column_names)
    print(results)
    