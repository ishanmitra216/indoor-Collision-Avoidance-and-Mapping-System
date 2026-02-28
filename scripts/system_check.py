import os

print("Checking system...")

print("Checking camera...")
os.system("python3 test_camera.py")

print("Checking database...")
os.system("sqlite3 ../database/robot.db '.tables'")

print("System check complete!")