from typing import Dict
from langchain_core.tools import tool

@tool
def assign_agent_to_task(agent_name: str, task: str) -> str:
        agent_module = __import__(f"agents.{agent_name}", fromlist=[agent_name])
        # Get agent function
        
        else:
            return agent_func(task)
    except AttributeError:
        return f"Error: Agent function '{agent_name}' not found in module"
    except Exception as e:
        return f"Error assigning task to agent {agent_name}: {str(e)}"