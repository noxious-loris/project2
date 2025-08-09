# 📊 Data Analyst API

A FastAPI-based application for uploading files, processing data, running analytics, and returning results.  
The app supports file uploads via an `/api/` endpoint and is containerized using Docker for easy deployment.

---

## 🚀 Features
- Upload `.txt` or `.csv` files via API
- Run custom data analysis using `pandas`, `matplotlib`, and `seaborn`
- Process data and return JSON and image results
- Deployable with **Docker**
- Easily expose a public endpoint with **ngrok** or cloud hosting

---

## 📂 Project Structure
project2/
│── app/
│ ├── main.py # FastAPI entry point
│ ├── processor.py # File processing logic
│ ├── utils/
│ ├── plot.py # Plot generation
│ ├── s3_handler.py # AWS S3 helper functions
│ ├── scraper.py # Web scraping logic
│── requirements.txt # Python dependencies
│── Dockerfile # Docker build instructions
│── README.md # Project documentation


---

## 🛠 Installation

### **1️⃣ Local Setup**
```bash
# Clone the repository
git clone https://github.com/<your-username>/project2.git
cd project2

# Create virtual environment
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn app.main:app --host 0.0.0.0 --port 8000


2️⃣ Run with Docker
# Build the Docker image
docker build -t my-fastapi-app .

# Run the container
docker run -p 8000:8000 my-fastapi-app

📡 API Usage
Upload a file
curl -X POST "http://127.0.0.1:8000/api/" \
  -F "file=@questions.txt"

🌍 Public Endpoint
To make it public temporarily:
pip install pyngrok
ngrok config add-authtoken <YOUR_TOKEN>
ngrok http 8000

📜 License
This project is licensed under the MIT License.
