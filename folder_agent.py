import json
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from helpers.config import api

class FolderAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api, temperature=0)
        self.base_path = r"C:\Users\HariVardhanaShubhash\Downloads\OneDrive_2025-10-09 1\Ops Bot"
        self.folder_details = self.load_folder_details()
    
    def load_folder_details(self):
        with open('helpers/detail.json', 'r') as f:
            return json.load(f)
    
    def get_folder_files(self, folder_name):
        folder_path = os.path.join(self.base_path, folder_name)
        if os.path.exists(folder_path):
            return [f for f in os.listdir(folder_path) if f.endswith(('.xlsx', '.xls', '.csv'))]
        return []
    
    def predict_best_folder_and_file(self, user_query):
        # Create context for LLM
        folder_context = ""
        for key, folder_info in self.folder_details.items():
            folder_name = folder_info['foldername']
            files = self.get_folder_files(folder_name)
            folder_context += f"Folder: {folder_name}\nDescription: {folder_info['Detail']}\nFiles: {files}\n\n"
        
        prompt = f"""Based on the user query and folder descriptions, predict the most relevant folder and file.

User Query: {user_query}

Available Folders and Files:
{folder_context}

Return only the folder name and most probable filename in this format:
FOLDER: [folder_name]
FILE: [filename]"""
        
        response = self.llm.invoke(prompt)
        return self.parse_response(response.content)
    
    def parse_response(self, response):
        lines = response.strip().split('\n')
        folder = None
        file = None
        
        for line in lines:
            if line.startswith('FOLDER:'):
                folder = line.replace('FOLDER:', '').strip()
            elif line.startswith('FILE:'):
                file = line.replace('FILE:', '').strip()
        
        return folder, file
    
    def get_file_path(self, user_query):
        folder, file = self.predict_best_folder_and_file(user_query)
        if folder and file:
            return os.path.join(self.base_path, folder, file)
        return None

# Usage
def find_best_file(user_query):
    agent = FolderAgent()
    return agent.get_file_path(user_query)