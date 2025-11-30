class SearchAgent:
    def __init__(self, source_config=None):
        self.source_config = source_config or {}

    async def search(self, topic: str, top_k: int = 10):
        # call external search API or arXiv client
        # return list of {'title','url','snippet','content','source','date'}
        return []
