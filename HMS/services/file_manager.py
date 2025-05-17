# file_manager.py - Handles saving and loading JSON data

import json
import os

def save_data(data, filename):
  
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # Ensure directories exist
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def load_data(filename):
    
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read().strip()
                if not content:
                    return []
                return json.loads(content)
        except json.JSONDecodeError:
            print(f"Warning: JSON decode error in file {filename}. Returning empty list.")
            return []
    else:
        return []
