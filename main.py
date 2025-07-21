from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def get_client_ip(request: Request):
    client_host = request.client.host
    return {"client_ip": client_host}
