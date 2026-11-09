# --- MONKEY-PATCH TO FIX GROQ CACHE_BREAKPOINT BUG ---
import crewai.llms.cache as _crewai_cache
_crewai_cache.mark_cache_breakpoint = lambda msg: msg
# -----------------------------------------------------

from crewai import Crew, Process
from src.agents_and_tasks import researcher, writer, research_task, write_task
import sys

def run_research(topic: str):
    # Assemble the crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        verbose=True,
    )
    
    # Kick off the research
    result = crew.kickoff(inputs={"topic": topic})
    
    # Save to file
    with open("report.md", "w", encoding="utf-8") as f:
        f.write(str(result))
        
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python src/crew.py 'Your research topic'")
        sys.exit(1)
    
    topic = sys.argv[1]
    print(f"\n🔍 Starting research on: {topic}\n")
    report = run_research(topic)
    print("\n" + "="*60)
    print("📄 FINAL REPORT SAVED TO report.md")
    print("="*60)
    print(report)
