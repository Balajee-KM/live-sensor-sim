from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow everyone to access your API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

data_store = []

@app.post("/data")
def receive_data(payload: dict):
    data_store.append(payload)
    return {"message": "Got it!"}

@app.get("/data")
def get_data():
    return data_store[-10:]

@app.get("/")
def home():
    return {"message": "Welcome! FastAPI server is live 🚀"}
