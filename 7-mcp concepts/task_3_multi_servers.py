#!/usr/bin/env python3
"""Task 3: Multiple MCP Servers - Orchestrating calculator and weather servers"""

import os
import asyncio
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

load_dotenv()

# ╔════════════════════════════════════════════╗
# ║     Multiple MCP Servers Architecture      ║
# ╚════════════════════════════════════════════╝
#
#              [User Query]
#                    │
#                    ▼
#            ┌──────────────┐
#            │  LangGraph   │
#            │ React Agent  │
#            └──────┬───────┘
#                   │
#         ┌─────────┴─────────┐
#         │MultiServerMCPClient│
#         └─────────┬─────────┘
#                   │
#      ┌────────────┴────────────┐
#      ▼                         ▼
# ┌──────────┐            ┌──────────┐
# │Calculator│            │ Weather  │
# │MCP Server│            │MCP Server│
# │    🔢    │            │    ☁️    │
# └──────────┘            └──────────┘
#
# The agent automatically routes to the appropriate server
# based on the query content and available tools

print("🌐 Task 3: Multiple MCP Servers\n")

# Import MCP adapter - uses real langchain-mcp-adapters package
try:
    from langchain_mcp_adapters.client import MultiServerMCPClient
except ImportError:
    print("⚠️ Creating mock MCP client for learning (install 'pip install langchain-mcp-adapters' for real)")

    class MultiServerMCPClient:
        def __init__(self, servers):
            self.servers = servers

        async def get_tools(self):
            """Mock tools from calculator and weather servers"""

            def mock_add(a: float, b: float) -> float:
                """Add two numbers"""
                return a + b

            def mock_multiply(a: float, b: float) -> float:
                """Multiply two numbers"""
                return a * b

            def mock_get_weather(city: str) -> str:
                """Get weather for a city"""
                weather_data = {
                    "London": "15°C, cloudy",
                    "New York": "22°C, sunny",
                    "Tokyo": "18°C, light rain",
                    "Paris": "20°C, partly cloudy",
                }
                return weather_data.get(city, f"20°C, clear skies (default for {city})")

            return [mock_add, mock_multiply, mock_get_weather]

# Initialize the LLM
model = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "openai/gpt-4o-mini"),
    base_url=os.getenv("OPENROUTER_API_BASE"),
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0,
    max_tokens=1000
)

print("Configuring multiple MCP servers:\n")

# TODO 1: Initialize MultiServerMCPClient with both servers
# Hint: Add both calculator and weather server configurations
client = MultiServerMCPClient(
    {
        "calculator": {
            "command": "python",
            "args": ["/root/code/mcp_servers/calculator_server.py"],
            "transport": "stdio",
        },
        "weather": {
            "command": "python",
            "args": ["/root/code/mcp_servers/weather_server.py"],
            "transport": "stdio",
        }
    }
)

async def run_multi_server_agent():
    """Create and run agent with multiple MCP servers"""

    print("📦 Loading tools from multiple servers...")

    # TODO 2: Get all tools from both servers
    # Hint: Use client.get_tools()
    tools = await client.get_tools()  # Replace ___ with client.get_tools()

    print(f"✅ Loaded {len(tools) if hasattr(tools, '__len__') else 'multiple'} tools from MCP servers")

    # TODO 3: Create react agent with all tools
    # Hint: Pass model and tools to create_agent
    agent = create_react_agent(model, tools)

    print("\n" + "=" * 60)
    print("TESTING MULTI-SERVER ORCHESTRATION:")
    print("=" * 60)

    # Test 1: Calculator query
    print("\nTest 1: Calculator MCP")
    calc_response = await agent.ainvoke({
        "messages": [("user", "What is 42 plus 58?")]
    })
    print(f"Response: {calc_response['messages'][-1].content}")

    # Test 2: Weather query
    print("\nTest 2: Weather MCP")
    weather_response = await agent.ainvoke({
        "messages": [("user", "What's the weather in London?")]
    })
    print(f"Response: {weather_response['messages'][-1].content}")

    # Test 3: Complex math
    print("\nTest 3: Complex Math")
    complex_response = await agent.ainvoke({
        "messages": [("user", "What's (3 + 5) x 12?")]
    })
    print(f"Response: {complex_response['messages'][-1].content}")

    # Test 4: Another weather query
    print("\nTest 4: Weather in Multiple Cities")
    cities_response = await agent.ainvoke({
        "messages": [("user", "Compare the weather in New York and Tokyo")]
    })
    print(f"Response: {cities_response['messages'][-1].content}")

    # Test 5: Mixed query
    print("\nTest 5: Mixed Query")
    mixed_response = await agent.ainvoke({
        "messages": [("user", "If it's 20°C in Paris and temperature rises by 5 degrees, what will it be?")]
    })
    print(f"Response: {mixed_response['messages'][-1].content}")

# Run the multi-server agent
if __name__ == "__main__":
    print("Starting Multi-Server MCP Orchestration...")
    print("This demonstrates how a single agent can use multiple MCP servers\n")

    # Run async function
    asyncio.run(run_multi_server_agent())

    print("\n" + "=" * 60)
    print("💡 KEY CONCEPTS:")
    print("- MultiServerMCPClient manages multiple MCP servers")
    print("- Each server exposes different tools")
    print("- Agent automatically selects appropriate tools")
    print("- Seamless orchestration across servers")
    print("- Extensible to many servers and domains")
    print("=" * 60)

    # Create marker file
    os.makedirs("/root/markers", exist_ok=True)
    with open("/root/markers/task3_multi_servers_complete.txt", "w") as f:
        f.write("TASK3_COMPLETE")