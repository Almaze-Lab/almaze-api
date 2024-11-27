from langchain_core.tools import tool

@tool
def read_file(filepath: str) -> str:
    """Read content from a file."""
        path = Path(filepath)
            return f.read()
