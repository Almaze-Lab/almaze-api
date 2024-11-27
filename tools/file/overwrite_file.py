
@tool
def overwrite_file(filepath: str, content: str) -> str:
    try:
        if not path.exists():
            return f"Error: File {filepath} does not exist"
            
    except Exception as e:
