# main.py
from fastapi import FastAPI
from client import MCPClient  # Make sure this file is named `mcp_client.py`
import asyncio
import uvicorn

app = FastAPI()

@app.get("/read-guide")
async def read_guide():
    async with MCPClient("http://localhost:8000/mcp") as client:
        templates = await client.list_resource_templates()
        guide_uri = templates[0].uriTemplate.replace("{doc_name}", "intro")
        data = await client.read_resource(guide_uri)
        return {"uri": guide_uri, "content": data}

@app.get("/list-templates")
async def list_templates():
    async with MCPClient("http://localhost:8000/mcp") as client:
        templates = await client.list_resource_templates()
        return {"templates": [t.uriTemplate for t in templates]}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
