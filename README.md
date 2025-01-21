# Doc Scraper MCP Server

The Doc Scraper is an MCP server that converts web documentation into markdown format using Jina.ai's API.

## Features

- Converts web pages to clean markdown
- Saves output to specified file path
- Handles URL fetching and error cases

## Usage

The server provides a single tool:

### scrape_docs

Scrapes documentation from a URL and saves it as markdown.

**Input Schema:**
```json
{
  "url": "string",       // URL of the documentation to scrape
  "output_path": "string" // Path to save the markdown file
}
```

**Example Request:**
```json
{
  "url": "https://example.com/docs",
  "output_path": "docs/example.md"
}
```

**Example Response:**
```json
{
  "content": [
    {
      "type": "text",
      "text": "Successfully scraped docs from https://example.com/docs and saved to docs/example.md"
    }
  ]
}
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   python -m doc_scraper
   ```

## Configuration

The server requires no special configuration and can be used immediately after installation.

## Dependencies

- Python 3.7+
- aiohttp
- pydantic
- mcp

## License

MIT License