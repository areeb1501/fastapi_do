from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Set up CORS
origins = [
    "http://localhost:3000",  # Allow specific origins (e.g., frontends running on localhost:3000)
    "https://example.com"     # You can also specify different domains
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allowed request methods
    allow_headers=["*"],  # Allowed request headers
)

@app.get("/")
async def home():
    return {"message": "Welcome to the FastAPI application!"}

class SquareInput(BaseModel):
    number: int

@app.post("/square")
async def square(data: SquareInput):
    result = data.number ** 2
    return {"number": data.number, "square": result}

@app.get("/info")
async def info():
    return {
        "creator": "Areeb",
        "description": "This is a simple FastAPI app with three endpoints.",
        "version": "1.0"
    }

# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
