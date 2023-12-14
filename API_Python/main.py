from fastapi import FastAPI
import pillsdetection as pd
from pydantic import BaseModel

class Image64(BaseModel):
    image64: str

class BoundingBoxes(BaseModel):
    boxes: list[list[float]]

# Start FastAPI
app = FastAPI()

@app.get("/", tags= ["general"])
def server_status():
    pills_model_status = "Offline" if pd.model is None else "Online"
    # Add other model statuses here (...)

    return {
        "server_status": "Online",
        "model_status": [
            {"pills_detection": pills_model_status}
            # Add other model statuses here (...)
        ]
    }

@app.post("/pills/predict-boxes", response_model=BoundingBoxes, tags=["pill detection"])
def predict_pills_bounding_boxes(img64: Image64):
    boxes = pd.get_prediction_boxes(img64.image64)
    return {"boxes": boxes}

@app.post("/pills/predict-image", response_model=Image64, tags=["pill detection"])
def predict_pills_image_with_bounding_boxes(img64: Image64):
    resImage64 = "TODO"
    return {"image64": resImage64}

