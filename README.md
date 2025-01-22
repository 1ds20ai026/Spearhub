# Spearhub

## **Predictive Analysis API for Manufacturing Operations**

### **Overview**
This project implements a RESTful API to predict machine downtime or production defects using a manufacturing dataset. The API includes endpoints for data upload, model training, and prediction.

---

### **Features**
- **Upload Dataset**: Upload a CSV file containing manufacturing data.
- **Train Model**: Train a machine learning model on the uploaded dataset.
- **Make Predictions**: Predict machine downtime based on input parameters (e.g., `Temperature` and `Run_Time`).

---

### **File Structure**
```
project-folder/
├── main.py                # Main FastAPI application
├── requirements.txt       # Python dependencies
├── manufacturing_data.csv # Sample dataset (optional)
├── models/
│   └── downtime_predictor_model.pkl # Trained model (auto-generated after training)
└── README.md              # Project documentation
```

---

### **Setup Instructions**

#### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

#### **2. Create a Virtual Environment**
Using `venv`:
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

Or using `conda`:
```bash
conda create -p ./venv python=3.9
conda activate ./venv
```

#### **3. Install Dependencies**
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

#### **4. Run the API**
Start the FastAPI server:
```bash
python main.py
```

Access the API at:
```
http://127.0.0.1:8000
```

---

### **Endpoints**

#### **1. Upload Dataset**
- **Endpoint**: `POST /upload`
- **Description**: Upload a CSV file containing manufacturing data.
- **Request**:
  - `form-data` with key `file` (file type).
- **Response**:
```json
{
    "message": "File uploaded successfully",
    "filename": "your_file_name.csv"
}
```

#### **2. Train Model**
- **Endpoint**: `POST /train`
- **Description**: Train the model on the uploaded dataset.
- **Response**:
```json
{
    "message": "Model trained successfully",
    "accuracy": 0.85,
    "f1_score": 0.88
}
```

#### **3. Make Predictions**
- **Endpoint**: `POST /predict`
- **Description**: Predict machine downtime based on input parameters.
- **Request**:
```json
{
    "Temperature": 80,
    "Run_Time": 120
}
```
- **Response**:
```json
{
    "Downtime": "Yes",
    "Confidence": 0.92
}
```

---

### **Sample Dataset**
A sample dataset (`manufacturing_data.csv`) is included in the repository. It contains the following columns:
- `Machine_ID`
- `Temperature`
- `Run_Time`
- `Downtime_Flag`

---

### **Testing the API**
Use **Postman** or **cURL** to test the endpoints:
- **Postman**:
  - Create `POST` requests to the endpoints.
  - Set the `Body` and `Headers` appropriately as described in the **Endpoints** section.
- **cURL**:
```bash
curl -X POST "http://127.0.0.1:8000/upload" -F "file=@manufacturing_data.csv"
curl -X POST "http://127.0.0.1:8000/train"
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"Temperature": 80, "Run_Time": 120}'
```

---

### **Dependencies**
- `fastapi`
- `uvicorn`
- `pandas`
- `scikit-learn`
- `joblib`

Install them via:
```bash
pip install -r requirements.txt
```

---


