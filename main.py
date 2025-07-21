from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
async def get_ip_and_redirect(request: Request):
    ip = request.client.host
    # Option 1: Pass IP to Streamlit as query param
    streamlit_url = f"https://web-production-db93.up.railway.app?ip={ip}"
    return RedirectResponse(url=streamlit_url)
