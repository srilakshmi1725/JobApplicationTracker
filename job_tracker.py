import sqlite3

# Connect to database (or create if it doesn't exist)
conn = sqlite3.connect('jobs.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY,
    company TEXT,
    job_title TEXT,
    status TEXT,
    date_applied TEXT,
    notes TEXT
)
''')

# Menu options
def menu():
    print("\n=== Job Application Tracker ===")
    print("1. Add New Job")
    print("2. View All Jobs")
    print("3. Update Job Status")
    print("4. Exit")

def add_job():
    company = input("Company name: ")
    title = input("Job title: ")
    status = input("Status (Applied/Interview/Rejected/Offer): ")
    date = input("Date applied (YYYY-MM-DD): ")
    notes = input("Notes: ")

    cursor.execute('''
    INSERT INTO applications (company, job_title, status, date_applied, notes)
    VALUES (?, ?, ?, ?, ?)
    ''', (company, title, status, date, notes))
    conn.commit()
    print("✅ Job added successfully!")

def view_jobs():
    cursor.execute('SELECT * FROM applications')
    jobs = cursor.fetchall()
    for job in jobs:
        print(f"\nID: {job[0]}, Company: {job[1]}, Title: {job[2]}, Status: {job[3]}, Date: {job[4]}, Notes: {job[5]}")

def update_status():
    job_id = input("Enter Job ID to update: ")
    new_status = input("New Status: ")
    cursor.execute('UPDATE applications SET status = ? WHERE id = ?', (new_status, job_id))
    conn.commit()
    print("✅ Status updated!")

# Run the CLI
while True:
    menu()
    choice = input("Enter choice: ")
    if choice == '1':
        add_job()
    elif choice == '2':
        view_jobs()
    elif choice == '3':
        update_status()
    elif choice == '4':
        break
    else:
        print("❌ Invalid choice. Try again.")
