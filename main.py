from fastapi import FastAPI, UploadFile, File
import pandas as pd
import joblib
from pydantic import BaseModel
import os


app = FastAPI()

MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "downtime_predictor_model.pkl")

os.makedirs(MODEL_DIR, exist_ok=True)

model = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None

@app.post("/upload")
async def upload_data(file: UploadFile = File(...)):
    data = pd.read_csv(file.file)
    data.to_csv("manufacturing_data.csv", index=False)
    return {"message": "File uploaded successfully", "filename": file.filename}

@app.post("/train")
async def train_model():
    global model
    try:
        data = pd.read_csv("manufacturing_data.csv")
        X = data[["Temperature", "Run_Time"]]
        y = data["Downtime_Flag"]
        
        from sklearn.linear_model import LogisticRegression
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import accuracy_score, f1_score

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LogisticRegression()
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        joblib.dump(model, MODEL_PATH)
        return {"message": "Model trained successfully", "accuracy": accuracy, "f1_score": f1}
    except Exception as e:
        return {"error": str(e)}

class PredictionRequest(BaseModel):
    Temperature: float
    Run_Time: float

@app.post("/predict")
async def predict(data: PredictionRequest):
    if not model:
        return {"error": "Model is not trained yet"}
    
    input_data = [[data.Temperature, data.Run_Time]]
    prediction = model.predict(input_data)
    confidence = model.predict_proba(input_data).max()
    
    return {
        "Downtime": "Yes" if prediction[0] == 1 else "No",
        "Confidence": round(confidence, 2)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
