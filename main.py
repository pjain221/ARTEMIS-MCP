import os
import asyncio
import logging
from typing import Optional
from fastmcp import FastMCP, Context
# from dotenv import load_dotenv
# from fastmcp.server.auth.providers import azure, jwt
# from databricks.sdk import WorkspaceClient
# from databricks.sdk.service.dashboards import GenieMessage, MessageStatus

load_dotenv(override=True)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global Config



# MCP Server
mcp = FastMCP(
    name="Artemis MCP",
    instructions=(
        "This is the Artemis MCP server. ARTEMIS: AI-powered Repository and Technology Management Integration System." \
        "It provides tools to interact with Github Actions, Access permissions to azure resources and Compliance issues."\
        "Use the tools below to perform specific tasks."
    ),
)

@mcp.resource("artemis://about")
def about_artemis() -> str:
    return (
        "Artemis MCP Server\n\n"
        "Artemis is a powerful tool for managing repositories and technology integrations. "
        "It provides features for interacting with GitHub Actions, Azure resources, and compliance management. "
    )

@mcp.tool
def call_artemis_access_agent(query: str) -> str:
    """
    Call the Artemis Access Agent with the given query. and retruns the response of what the artemis agent does.
    """
    # Placeholder for actual implementation

    return f"Access Agent Response to '{query}'"




if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
