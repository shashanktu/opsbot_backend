from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ["gemini_API"])

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def process_query(request: QueryRequest):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""You are a data analyst assistant. Based on the user query, provide guidance on what type of data they might need and suggest which folder/file to look in.

Available folders:
- Account Details: Employee details, project allocation, status
- Bench Report: Bench employees, skills, availability  
- Certifications: Employee certifications, dates, codes
- GT's Allocation: Graduate trainee allocations
- RRF: Resource request forms
- Utilization: Monthly utilization dashboards

User Query: {request.query}

Provide a helpful response about where to find this data."""
        
        response = model.generate_content(prompt)
        return {"success": True, "result": response.text}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.get("/")
async def root():
    return {"message": "Lightweight Excel Query API is running"}