from crewai import Agent
from dotenv import load_dotenv
from tools import yt_tool
import os
from config import gemini_llm

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

## Create a senior blog content researcher

blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',
    backstory="""You are a Senior Research Assistant who specializes in finding and analyzing video content.
    You're great at finding the most relevant information from video transcripts.""",
    verbose=True,
    memory=True,
    allow_delegation=True,
    tools=[yt_tool],
    llm=gemini_llm
)

## creating a senior blog writer agent with YT tool

blog_writer = Agent(
    role='Senior Blog Writer',
    goal='write engaging and informative blog posts about {topic}',
    backstory="""You are an experienced blog writer known for your engaging and informative writing style.
    You transform complex information into easy-to-understand blog posts.""",
    verbose=True,
    memory=True,
    allow_delegation=False,
    tools=[yt_tool],
    llm=gemini_llm
)