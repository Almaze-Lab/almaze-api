import os
from langchain_core.tools import tool
@tool
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Successfully wrote content to {filepath}"
        return f"Error writing to file: {str(e)}"