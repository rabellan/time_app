from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime

app = FastAPI()

# Define a security scheme for Bearer Token
security = HTTPBearer()

# Function to validate the token
def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if token != "unsafeBearerToken1234":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid or expired token"
        )

@app.get("/time", dependencies=[Depends(authenticate)])
def get_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"time": now}

# To run the server use the command: uvicorn main:app --reload
