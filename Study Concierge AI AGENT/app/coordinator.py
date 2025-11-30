import uuid
from .agents.search_agent import SearchAgent
from .agents.summarizer_agent import SummarizerAgent
from .agents.quiz_agent import QuizAgent
from .agents.memory_agent import MemoryAgent
from .utils.logging import tracer

class CoordinatorAgent:
    def __init__(self):
        self.search = SearchAgent()
        self.summarizer = SummarizerAgent()
        self.quiz = QuizAgent()
        self.memory = MemoryAgent()

    async def handle_mission(self, mission: dict):
        trace_id = str(uuid.uuid4())
        with tracer.start_as_current_span("mission", attributes={"trace_id": trace_id}):
            topic = mission.get("topic")
            # 1. Search
            hits = await self.search.search(topic)
            # 2. Ingest & Summarize (pick top K)
            summary = await self.summarizer.summarize(hits, topic)
            # 3. Generate Quiz
            quiz = await self.quiz.generate(summary)
            # 4. Persist memory
            await self.memory.write({"topic": topic, "summary_meta": summary.meta})
            # 5. Consolidate result
            result = {"summary": summary.text, "quiz": quiz.items}
            return SimpleNamespace(id=trace_id, result=result)
