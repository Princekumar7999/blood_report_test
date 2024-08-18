from langchain.tools import BaseTool

class BloodTestAnalyzer(BaseTool):
    name = "Blood Test Analyzer"
    description = "Analyzes blood test results from PDF text and provides a summary"

    def _run(self, blood_test_data: str):
       
        analysis = "Analysis of blood test:\n"
        
        
        if "hemoglobin" in blood_test_data.lower():
            analysis += "- Hemoglobin levels were measured\n"
        if "cholesterol" in blood_test_data.lower():
            analysis += "- Cholesterol levels were checked\n"
        if "glucose" in blood_test_data.lower():
            analysis += "- Glucose levels were assessed\n"
        
        analysis += "\nNote: This is a basic analysis. Please consult with a healthcare professional for accurate interpretation."
        return analysis

    def _arun(self, blood_test_data: str):
       
        raise NotImplementedError("BloodTestAnalyzer does not support async")