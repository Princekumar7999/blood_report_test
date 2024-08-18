from crewai import Agent
from tools.blood_test_analyzer import BloodTestAnalyzer

blood_test_agent = Agent(
    role='Blood Test Analyzer',
    goal='Accurately interpret blood test results',
    backstory='Expert in analyzing blood test reports with years of experience in laboratory medicine.',
    tools=[BloodTestAnalyzer()],
    verbose=True
)