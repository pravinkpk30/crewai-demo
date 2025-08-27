from crewai import Crew, Process

# Import agents after they're defined
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,  # Optional: Sequential task execution is default
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

if __name__ == "__main__":
    # Start the task execution process with enhanced feedback
    result = crew.kickoff(inputs={'topic': 'Napkin ai'})
    print(result)