from langchain.tools import BaseTool
from duckduckgo_search import ddg

class WebResearcher(BaseTool):
    name = "Web Researcher"
    description = "Searches the web for relevant health articles"

    def _run(self, query: str):
        results = ddg(query, max_results=5)
        return [{"title": r["title"], "link": r["href"]} for r in results]

    def _arun(self, query: str):
       
        raise NotImplementedError("WebResearcher does not support async")