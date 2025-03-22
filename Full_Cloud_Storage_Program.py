import os
import boto3
import sqlite3
from flask import Flask, request, jsonify

# Initialize Flask App
app = Flask(__name__)

# AWS S3 Configuration (Set up your credentials in ~/.aws/credentials)
AWS_REGION = "us-east-1"
S3_BUCKET = "your-s3-bucket-name"

s3_client = boto3.client("s3", region_name=AWS_REGION)

# Database setup for user management
DB_FILE = "users.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route("/upload", methods=["POST"])
def upload_file():
    """Uploads a file to AWS S3"""
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    s3_client.upload_fileobj(file, S3_BUCKET, file.filename)

    return jsonify({"message": f"File '{file.filename}' uploaded successfully!"})

@app.route("/list", methods=["GET"])
def list_files():
    """Lists all files stored in AWS S3"""
    response = s3_client.list_objects_v2(Bucket=S3_BUCKET)

    if "Contents" in response:
        files = [obj["Key"] for obj in response["Contents"]]
        return jsonify({"files": files})
    else:
        return jsonify({"message": "No files found."})

@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    """Downloads a file from AWS S3"""
    download_path = os.path.join("downloads", filename)
    s3_client.download_file(S3_BUCKET, filename, download_path)

    return jsonify({"message": f"File '{filename}' downloaded successfully!"})

@app.route("/share", methods=["POST"])
def share_file():
    """Generates a temporary URL for sharing a file"""
    data = request.json
    filename = data.get("filename")

    if not filename:
        return jsonify({"error": "Filename is required"}), 400

    url = s3_client.generate_presigned_url(
        "get_object",
        Params={"Bucket": S3_BUCKET, "Key": filename},
        ExpiresIn=3600  # Link expires in 1 hour
    )

    return jsonify({"shareable_link": url})

if __name__ == "__main__":
    app.run(debug=True)