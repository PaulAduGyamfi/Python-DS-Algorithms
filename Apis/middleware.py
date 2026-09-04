import uuid
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, Header, HTTPException, Request

load_dotenv()
app = FastAPI()
real_api_key = os.environ["REAL_API_KEY"]

def api_key_validator(api_key: str = Header(...)):
        if api_key != real_api_key:
            raise HTTPException(status_code=401, detail="invalid api key")

@app.middleware("http")
async def add_run_id(request: Request, call_next):
    run_id = str(uuid.uuid4())
    request.state.run_id = run_id
    response = await call_next(request)
    response.headers["Run-Id"] = run_id
    return response

@app.get("/info", dependencies=[Depends(api_key_validator)])
def secure_endpoint(request: Request):
    return {"status" : "ok", "run_id" : request.state.run_id}
