class SummarizerAgent:
    def __init__(self, llm_client=None, retriever=None):
        self.llm = llm_client
        self.retriever = retriever

    async def summarize(self, hits, topic):
        # chunk + embed + retrieve + LLM prompt to produce structured summary
        # return object with .text and .meta
        return SimpleNamespace(text="...", meta={"sources": []})
