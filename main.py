from crewai import Crew, Task
from agents.blood_test_agent import blood_test_agent
from agents.web_research_agent import web_research_agent
from agents.health_advisor_agent import health_advisor_agent
from utils.file_reader import read_blood_test_report

def main():
   
    blood_test_url = ""
    
   
    blood_test_data = read_blood_test_report(blood_test_url)

   
    
   
    analyze_blood_test = Task(
        description='Analyze the blood test report and summarize findings',
        agent=blood_test_agent
    )

    research_articles = Task(
        description='Search for relevant health articles based on blood test analysis',
        agent=web_research_agent
    )

    provide_recommendations = Task(
        description='Compile health recommendations based on analysis and research',
        agent=health_advisor_agent
    )

    
    health_crew = Crew(
        agents=[blood_test_agent, web_research_agent, health_advisor_agent],
        tasks=[analyze_blood_test, research_articles, provide_recommendations]
    )

   
    result = health_crew.kickoff()

    print(result)

if __name__ == "__main__":
    main()

    if uploaded_file is not None:
        try:
            st.write("Analyzing your blood test report...")
            
          
            pdf_content = extract_text_from_pdf(uploaded_file)
            
           
            result = analyze_blood_test(pdf_content)
            
            st.write("Analysis complete!")
            st.write(result)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")