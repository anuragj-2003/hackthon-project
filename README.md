# hackthon-project

A comprehensive system for managing school activities involving **Headmaster, Teachers, and Students**, built with:
- **Backend:** FastAPI + PostgreSQL
- **Frontend:** React + Vite + Bootstrap CSS
- **Database:** PostgreSQL

---

## ⚙️ 1. System Requirements
Ensure you have the following installed on your system:
- **Python 3.10+** (recommended 3.12)
- **Node.js 18+** (recommended 20)
- **PostgreSQL Database**
- **Git**

---

## 🗄️ 2. Backend Setup – FastAPI + PostgreSQL

### 🧑‍💻 Step 1: Clone the Repository
```bash
git clone <repository_url>
cd hackathon-project/backend
```

### 3. Install Dependicies
``` bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL Database
```bash
CREATE DATABASE school_management;

DATABASE_URL = "postgresql://username:password@localhost/school_management"
```

### 5. Run the Backend Server
```bash
uvicorn main:app --reload
```

### 6. Server will start in : 
```bash
http://127.0.0.1:8000
```




# Frontend Setup – Vite + React + Bootstrap CSS


### 1. Navigate to Frontend Directory
```bash
cd ../frontend
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Run the Frontend Development Server
```bash
npm run dev
```
### 4. Open the developement link in :
```bash
http://localhost:5173
```

# Database (PostgreSQL) Setup Summary
```bash
CREATE DATABASE school_management;

DATABASE_URL = "postgresql://username:password@localhost/school_management"
```


# Running full stack application
## start backend
```bash
cd backend
source myenv/bin/activate
uvicorn main:app --reload
```

## start frontend
```bash
cd frontend
npm run dev
```




