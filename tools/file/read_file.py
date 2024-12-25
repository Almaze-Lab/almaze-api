from langchain_core.tools import tool

@tool
def read_file(filepath: str) -> str:
        path = Path(filepath)
            return f.read()
