[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/askjohngeorge-mcp-doc-scraper-badge.png)](https://mseep.ai/app/askjohngeorge-mcp-doc-scraper)

# Doc Scraper MCP Server
[![smithery badge](https://smithery.ai/badge/@askjohngeorge/mcp-doc-scraper)](https://smithery.ai/server/@askjohngeorge/mcp-doc-scraper)

A Model Context Protocol (MCP) server that provides documentation scraping functionality. This server converts web-based documentation into markdown format using jina.ai's conversion service.

## Features

- Scrapes documentation from any web URL
- Converts HTML documentation to markdown format
- Saves the converted documentation to a specified output path
- Integrates with the Model Context Protocol (MCP)

## Installation

### Installing via Smithery

To install Doc Scraper for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@askjohngeorge/mcp-doc-scraper):

```bash
npx -y @smithery/cli install @askjohngeorge/mcp-doc-scraper --client claude
```

1. Clone the repository:

```bash
git clone https://github.com/askjohngeorge/mcp-doc-scraper.git
cd mcp-doc-scraper
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the dependencies:

```bash
pip install -e .
```

## Usage

The server can be run using Python:

```bash
python -m mcp_doc_scraper
```

### Tool Description

The server provides a single tool:

- **Name**: `scrape_docs`
- **Description**: Scrape documentation from a URL and save as markdown
- **Input Parameters**:
  - `url`: The URL of the documentation to scrape
  - `output_path`: The path where the markdown file should be saved

## Project Structure

```
doc_scraper/
├── __init__.py
├── __main__.py
└── server.py
```

## Dependencies

- aiohttp
- mcp
- pydantic

## Development

To set up the development environment:

1. Install development dependencies:

```bash
pip install -r requirements.txt
```

2. The server uses the Model Context Protocol. Make sure to familiarize yourself with [MCP documentation](https://modelcontextprotocol.io/).

## License

MIT License
