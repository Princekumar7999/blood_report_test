from crewai import Agent
from tools.health_advisor import HealthAdvisor

health_advisor_agent = Agent(
    role='Health Advisor',
    goal='Provide personalized health recommendations',
    backstory='Experienced in creating health plans based on medical data and research.',
    tools=[HealthAdvisor()],
    verbose=True
)