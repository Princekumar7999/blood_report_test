from langchain.tools import BaseTool

class HealthAdvisor(BaseTool):
    name = "Health Advisor"
    description = "Provides health recommendations based on analysis and research"

    def _run(self, analysis: str, articles: list):
        
        recommendations = "Based on the analysis and research:\n"
        recommendations += "1. Maintain a balanced diet\n"
        recommendations += "2. Exercise regularly\n"
        recommendations += "3. Get enough sleep\n"
        return recommendations

    def _arun(self, analysis: str, articles: list):
        
        raise NotImplementedError("HealthAdvisor does not support async")