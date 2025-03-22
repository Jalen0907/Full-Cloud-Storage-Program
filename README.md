# Full-Cloud-Storage-Program
🌩 Cloud File Storage & Sharing System
This project is a cloud-based file storage system that allows users to upload, download, list, and share files using Amazon S3. It provides a simple Flask API to interact with cloud storage efficiently.

📌 Features
✅ Upload Files - Users can upload files to AWS S3.
✅ List Stored Files - Users can retrieve a list of all files stored in the cloud.
✅ Download Files - Users can download any file from S3.
✅ Share Files - Generates a temporary shareable link (valid for 1 hour).
✅ Database for User Management - Uses SQLite to manage users.

🛠 Tech Stack
Python - Backend programming
Flask - REST API framework
AWS S3 - Cloud storage service
Boto3 - AWS SDK for Python
SQLite - Lightweight database for user management
🚀 Setup Instructions
1️⃣ Prerequisites
Ensure you have the following installed:

Python 3.7+
AWS Account & S3 Bucket
AWS CLI (Configured with aws configure)
2️⃣ Install Dependencies
Run the following command in the project directory:


pip install boto3 flask sqlite3
3️⃣ Set Up AWS S3
Create an S3 bucket in AWS.
Update the S3_BUCKET name in app.py.
4️⃣ Run the Application
Start the Flask server:

bash
Copy
Edit
python app.py
