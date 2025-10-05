import os
import asyncio
import logging
from typing import Optional
from fastmcp import FastMCP, Context
import requests
import base64
# from dotenv import load_dotenv
# from fastmcp.server.auth.providers import azure, jwt
# from databricks.sdk import WorkspaceClient
# from databricks.sdk.service.dashboards import GenieMessage, MessageStatus
# load_dotenv(override=True)

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
def access_provider(user:str, repository: str) -> str:
    """
    Tool to provide and revoke access to azure resources based on the query and user.
    user: user to whom access is to be provided or revoked
    repository: repository for which access is to be provided or revoked
    """

    pat_token_os = os.getenv('AZURE_DEVOPS_PAT')
    pat_token = base64.b64encode(f":{pat_token_os}".encode()).decode()
    url = "https://vsaex.dev.azure.com/reply-hackathon/_apis/userentitlements?api-version=7.1"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {pat_token}"
    }
    payload = {
        "accessLevel": {
            "licensingSource": "account",
            "accountLicenseType": "express"
        },
        "extensions": [
            {
                "id": "ms.feed"
            }
        ],
        "user": {
            "principalName": "d.hoglund@reply.com",
            "subjectKind": "user"
        },
        "projectEntitlements": [
            {
                "group": {
                    "groupType": "projectContributor"
                },
                "projectRef": {
                    "id": "27682584-7e8b-44d0-9670-297525085096"
                }
            }
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error providing access: {e}")
        return f"Error providing access: {e}"
    return f"Access provided to {user} for repository {repository}"


@mcp.tool
def call_artemis_access_agent(query: str) -> str:
    """
    Call the Artemis Access Agent with the given query. and retruns the response of what the artemis agent does.
    """
    # Placeholder for actual implementation

    return f"Access Agent Response to '{query}'"




if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
