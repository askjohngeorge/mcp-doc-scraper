import logging
import os
import aiohttp
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool
from pydantic import BaseModel


class ScrapeDocsInput(BaseModel):
    url: str
    output_path: str


async def serve() -> None:
    logger = logging.getLogger(__name__)
    server = Server("doc-scraper")

    @server.list_tools()
    async def list_tools() -> list[Tool]:
        return [
            Tool(
                name="scrape_docs",
                description="Scrape documentation from a URL and save as markdown",
                inputSchema=ScrapeDocsInput.schema(),
            )
        ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[TextContent]:
        if name != "scrape_docs":
            raise ValueError(f"Unknown tool: {name}")
        url = arguments["url"]
        output_path = arguments["output_path"]
        try:
            # Use jina.ai to convert URL to markdown
            jina_url = f"https://r.jina.ai/{url}"
            async with aiohttp.ClientSession() as session:
                async with session.get(jina_url) as response:
                    if response.status != 200:
                        return [
                            TextContent(
                                type="text",
                                text=f"Failed to fetch content: {response.status}",
                            )
                        ]
                    content = await response.text()
            # Ensure output directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            # Save markdown content
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)
            return [
                TextContent(
                    type="text",
                    text=f"Successfully scraped docs from {url} and saved to {output_path}",
                )
            ]
        except Exception as e:
            logger.exception("Error while scraping documentation.")
            return [TextContent(type="text", text=f"Error: {str(e)}")]

    options = server.create_initialization_options()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, options, raise_exceptions=True)
