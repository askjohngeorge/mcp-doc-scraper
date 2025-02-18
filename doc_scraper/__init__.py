import asyncio
import logging
from .server import serve


async def main():
    """MCP Doc Scraper - Documentation scraping functionality for MCP"""
    logging.basicConfig(level=logging.INFO)
    await serve()


if __name__ == "__main__":
    asyncio.run(main())
