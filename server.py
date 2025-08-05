from mcp.server.fastmcp import FastMCP
import base64

mcp = FastMCP(name="hello_mcp", stateless_http=True)

docs = {
    "intro": "This is a simple example of a stateless MCP server.",
    "readme": "This server provides a greeting tool that returns a simple message.",
    "guide": "You can use the greeting tool to get a friendly message.",
}

@mcp.resource("docs://documents", mime_type="application/json")
def list_docs():
    """List available documentation."""
    return list(docs.keys())

@mcp.resource("docs://documents/{doc_name}", mime_type="application/json")
def read_doc(doc_name: str):
    """Read a specific document."""
    if doc_name in docs:
        content = docs[doc_name]
        binary_data = base64.b64encode(content.encode("utf-8")).decode("utf-8")
        return {"name": doc_name, "binary": binary_data}
    else:
        raise mcp.ResourseNotFound(f"Document {doc_name} not found.")

mcp_server = mcp.streamable_http_app()
