from langchain_core.tools import tool

@tool
def delete_file(filepath: str) -> str:
    """Delete a file."""
    try:
            return f"Error: File {filepath} does not exist"
        path.unlink()
        return f"Successfully deleted {filepath}"
