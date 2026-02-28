import os
from db_manager import DBManager

def run_schema(file_path):

    db = DBManager()

    with open(file_path, "r") as f:
        sql_script = f.read()

    db.cursor.executescript(sql_script)
    db.conn.commit()
    db.close()


if __name__ == "__main__":

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    schemas_dir = os.path.join(base_dir, "schemas")

    run_schema(os.path.join(schemas_dir, "pose_schema.sql"))
    run_schema(os.path.join(schemas_dir, "map_schema.sql"))

    print("Database initialized successfully.")