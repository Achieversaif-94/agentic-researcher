from crewai.tools import BaseTool
from ddgs import DDGS

class WebSearchTool(BaseTool):
    name: str = "Web Search"
    description: str = "Useful to search the internet for current events and factual information. Returns the top 3 search results with titles, snippets, and URLs."

    def _run(self, query: str) -> str:
        try:
            results = DDGS().text(query, max_results=3)
            if not results:
                return f"No results found for '{query}'."
                
            formatted_results = ""
            for i, res in enumerate(results, 1):
                formatted_results += f"\n--- Result {i} ---\n"
                formatted_results += f"Title: {res.get('title')}\n"
                formatted_results += f"Snippet: {res.get('body')}\n"
                formatted_results += f"URL: {res.get('href')}\n"
            
            return formatted_results
        except Exception as e:
            return f"Search failed: {str(e)}"
