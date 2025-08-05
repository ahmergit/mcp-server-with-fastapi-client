# client.py
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession, types
import asyncio
from contextlib import AsyncExitStack
from typing import Any
from pydantic import AnyUrl
import json

class MCPClient:
    def __init__(self, url):
        self.url = url
        self.stack = AsyncExitStack()
        self._sess = None

    async def __aenter__(self):
        read, write, _ = await self.stack.enter_async_context(
            streamablehttp_client(self.url)
        )
        self._sess = await self.stack.enter_async_context(
            ClientSession(read, write)
        )
        await self._sess.initialize()
        return self

    async def __aexit__(self, *args):
        await self.stack.aclose()

    async def list_resource_templates(self) -> list[types.ResourceTemplate]:
        assert self._sess, "Session not available"
        result: types.ListResourceTemplatesResult = await self._sess.list_resource_templates()
        return result.resourceTemplates

    async def read_resource(self, uri: str) -> str:
        assert self._sess, "Session not available"
        _url = AnyUrl(uri)
        result = await self._sess.read_resource(_url)
        resource = result.contents[0]

        if isinstance(resource, types.TextResourceContents):
            try:
                payload = json.loads(resource.text)
                if "binary" in payload:
                    return payload["binary"]
                return resource.text
            except Exception as e:
                return f"[Error reading resource] {e}"

        return "[Unsupported content type]"
