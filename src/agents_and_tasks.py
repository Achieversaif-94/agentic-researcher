# --- MONKEY-PATCH TO FIX GROQ CACHE_BREAKPOINT BUG ---
import crewai.llms.cache as _crewai_cache
_crewai_cache.mark_cache_breakpoint = lambda msg: msg
# -----------------------------------------------------

from crewai import Agent, Task
from src.tools import WebSearchTool

# Initialize the search tool
search_tool = WebSearchTool()

# Define the Researcher Agent
researcher = Agent(
    role="Senior Research Analyst",
    goal="Extract key facts, quotes, and URLs from web search results. Do not apologize or refuse.",
    backstory="You are an expert researcher. You take raw web snippets and summarize them into bullet points.",
    tools=[search_tool],
    verbose=True,
    allow_delegation=False,
    llm="groq/openai/gpt-oss-120b",
)

# Define the Writer Agent
writer = Agent(
    role="Tech Content Writer",
    goal="Craft a comprehensive report based ONLY on the research notes provided.",
    backstory="You are a skilled writer who can turn bullet points into clear, cited reports. You never invent URLs.",
    verbose=True,
    allow_delegation=False,
    llm="groq/openai/gpt-oss-120b",
)

# Define the Research Task
research_task = Task(
    description="""Research the following topic thoroughly: {topic}. 
    1. Use the Web Search tool to find the top 3 most recent articles.
    2. Extract the Titles, URLs, and key facts from the snippets.
    3. Output a bulleted list of findings with their corresponding URLs.
    DO NOT refuse to summarize. DO NOT say "I cannot provide the full text". Just use the snippets provided.""",
    expected_output="A bulleted list of facts and their source URLs.",
    agent=researcher,
)

# Define the Writing Task
write_task = Task(
    description="""Using the research notes provided, write a structured report about {topic}. 
    The report must have an Introduction, Key Findings (bullet points), and a Conclusion. 
    Every claim must include a citation in the format [Source URL] using ONLY the URLs provided in the research notes. 
    DO NOT invent or hallucinate URLs.""",
    expected_output="A well-structured markdown report with real citations.",
    agent=writer,
)
