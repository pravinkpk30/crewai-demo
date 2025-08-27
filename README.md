# CrewAI Project with Gemini Integration

A project demonstrating how to create AI agents using CrewAI with Google's Gemini model for YouTube content research and blog writing.

## Prerequisites

- Python 3.8+
- [UV](https://github.com/astral-sh/uv) package manager
- Google API key with access to Gemini models

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd crewai-demo
```

2. Set up environment variables:
```bash
cp .env.example .env
```

3. Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

4. Install dependencies:
```bash
uv pip install -r requirements.txt
```

5. Create a .env file and add your API key
```bash
GOOGLE_API_KEY=your_google_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

6. Run the script:
```bash
python crew.py
```

# Project Structure

- agents.py: Contains the agents for the project
- tasks.py: Contains the tasks for the project
- tools.py: Contains the tools for the project
- crew.py: Main script for running the project
- .env: Environment variables
- requirements.txt: Project dependencies
- .env.example: Example environment variables
- config.py: Configuration file

# Creating Components

1. Agents
```python
from crewai import Agent
from config import gemini_llm

researcher = Agent(
    role='Research Specialist',
    goal='Find and analyze information about {topic}',
    backstory="""You are an expert researcher with a keen eye for detail.""",
    verbose=True,
    llm=gemini_llm
)
``` 

2. Create Tasks
```python
from crewai import Task

research_task = Task(
    description="Research information about {topic}",
    expected_output="A detailed report on {topic}",
    agent=researcher
)
```

3. Setup Tools
```python
from crewai_tools import tool
@tool
def search_web(query: str) -> str:
    """Search the web for information."""
    # Implementation here
    return search_results
```

4. Create and Run the Crew
```python
from crewai import Crew
from agents import researcher
from tasks import research_task

crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=2
)

result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
print(result)
```

5. Agent Configuration
```python
from crewai import LLM
import os

gemini_llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.1,
    api_key=os.getenv("GOOGLE_API_KEY")
)
```



