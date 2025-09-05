
# custom_web_search.py

import requests
from openai import OpenAI
from openai.agents import Agent, function_tool

client = OpenAI()

# ---------------------------
# Tavily Web Search Function Tool
# ---------------------------
@function_tool
def tavily_search(query: str, max_results: int = 5):
    """
    Perform a web search using Tavily API and return results.
    """
    API_KEY = "YOUR_TAVILY_API_KEY"
    url = "https://api.tavily.com/search"
    
    headers = {"Content-Type": "application/json"}
    payload = {
        "api_key": API_KEY,
        "query": query,
        "max_results": max_results
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        results = response.json().get("results", [])
        
        if not results:
            return {"message": "No results found."}

        # Return top results
        return {
            "query": query,
            "results": [
                {"title": r.get("title"), "url": r.get("url")}
                for r in results
            ]
        }
    except Exception as e:
        return {"error": str(e)}
