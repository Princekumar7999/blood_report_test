from crewai import Agent
from tools.web_researcher import WebResearcher

web_research_agent = Agent(
    role='Web Researcher',
    goal='Find relevant health articles based on blood test results',
    backstory='Skilled at searching and curating health information from reputable sources.',
    tools=[WebResearcher()],
    verbose=True
)