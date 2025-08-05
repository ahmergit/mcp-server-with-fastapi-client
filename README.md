# MCP Server with FastAPI Client

A lightweight and modular implementation of an **MCP (Model Context Protocol)** server with a FastAPI-based client. This project demonstrates how to expose and consume MCP tools and resources using a modern Python async stack.

It uses the high-performance **FastAPI** framework for the client and integrates the **MCP Python SDK** for server-side logic. Dependency management is handled using the blazing-fast **[uv](https://github.com/astral-sh/uv)** package manager.

Ideal for experimenting with tool invocation, resource access, and extending server capabilities in structured AI-driven workflows.


##  Features

- **FastAPI Client**: Lightweight, async web API built using FastAPI for easy integration and extensibility.
- **MCP Server Integration**: Interacts with an MCP (Model Context Protocol) server using the `mcp` Python SDK over HTTP.
- **Modular Design**: Code is cleanly separated into reusable client and server logic for easy customization.
- **uv Dependency Manager**: Uses [uv](https://github.com/astral-sh/uv) for fast and reliable dependency management with modern Python tooling.


## Getting Started

### Prerequisites
- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package manager
- FastAPI
- Uvicorn

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ahmergit/mcp-server-with-fastapi-client.git
   ```
2. Install dependencies using uv:
   ```bash
   uv add install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```bash
   uv run uvicorn main:app --reload
   ```
4. Run the MCP server :
    ```bash
    uv run uvicorn server:mcp_server --reload

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss improvements or bugs.
