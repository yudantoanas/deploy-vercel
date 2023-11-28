from fastapi import FastAPI, HTTPException, Request
import pandas as pd

# key untuk akses endpoint
key = "secret123"

# panggil class FastAPI
app = FastAPI()

# load data csv
data = pd.read_csv('data.csv')

# define url/endpoint
@app.get('/')
def handler(request: Request):
    # retrieve headers content from request
    headers = request.headers

    # retrieve User-Agent key in headers
    agent = headers.get("User-Agent")
    
    token = headers.get("Token")

    if token == None: # jika key Token tidak ada dalam headers
        raise HTTPException(status_code=500, detail="belum login")
    else: # jika ada key Token
        if token != key: # jika token != key, raise error/exception
            raise HTTPException(status_code=500, detail="Key tidak sesuai")
        else:
            return {
                "message": "halaman utama",
                "agent": agent # display value 'agent' in response
            }

@app.get('/data')
def handler():
    return data.to_dict(orient='records')

@app.get('/home/{user}')
def handler(user):
    if user == "yuda":
        return {
            "message": "hello home",
            "user": user
        }
    else:
        # handle error
        raise HTTPException(status_code=400, detail="not found")
    