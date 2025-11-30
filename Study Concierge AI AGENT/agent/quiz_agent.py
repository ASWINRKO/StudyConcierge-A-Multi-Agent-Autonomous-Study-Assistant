class QuizAgent:
    async def generate(self, summary_obj, num_mcq=10):
        # Use LLM to produce MCQs and answers; run critic loop for plausibility
        return SimpleNamespace(items=[])
