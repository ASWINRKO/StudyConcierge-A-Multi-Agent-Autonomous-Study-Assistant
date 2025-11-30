from fastapi import FastAPI
from app.coordinator import CoordinatorAgent
from app.tools.mcp_server import register_tools

app = FastAPI(title="StudyConcierge API")
coord = CoordinatorAgent()
register_tools()  # expose MCP tool endpoints

@app.post("/mission")
async def run_mission(payload: dict):
    """Accepts {'topic': str, 'mode': 'summary+quiz'}"""
    trace = await coord.handle_mission(payload)
    return {"status": "ok", "trace_id": trace.id, "result": trace.result}
