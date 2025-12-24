
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
import os
from monitor import WebsiteMonitor

app = FastAPI(title="EduMonitor Web")

# Templates
templates = Jinja2Templates(directory="templates")

# Monitor
monitor = WebsiteMonitor()
# Load URLs (Ensure the file exists in the same directory or provide full path)
URL_FILE = '지역교육청_url.txt'
monitor.load_urls(URL_FILE)

# API Models
class CheckResponse(BaseModel):
    network_error: bool
    results: list[dict]

@app.get("/")
async def read_root(request: Request):
    urls = monitor.get_urls()
    return templates.TemplateResponse("index.html", {"request": request, "urls": urls})

@app.get("/api/check")
async def check_websites():
    # Note: monitor.run_check is synchronous (uses requests/socket)
    # FastAPI runs sync path operations in a threadpool, so this is safe and won't block the loop.
    result = monitor.run_check()
    
    # Transform result for frontend easy consumption
    # result structure from monitor.py: {'network_error': bool, 'failed_sites': [{'name', 'url', 'error'}]}
    # We want to return status for ALL sites, not just failed ones.
    
    all_results = []
    urls = monitor.get_urls()
    
    if result['network_error']:
        # If network error, mark all as failed (or unknown)
        for name, url in urls.items():
             all_results.append({
                "name": name, 
                "url": url, 
                "status": "error", 
                "msg": "Network Error"
            })
    else:
        # Map failures for quick lookup
        failed_map = {item['name']: item['error'] for item in result['failed_sites']}
        
        for name, url in urls.items():
            if name in failed_map:
                all_results.append({
                    "name": name, 
                    "url": url, 
                    "status": "error", 
                    "msg": failed_map[name]
                })
            else:
                all_results.append({
                    "name": name, 
                    "url": url, 
                    "status": "ok", 
                    "msg": "OK"
                })

    return JSONResponse(content={"network_error": result['network_error'], "results": all_results})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
