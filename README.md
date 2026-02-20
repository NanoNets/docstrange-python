# Docstrange Python SDK

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/docstrange-api.svg?label=pypi%20(stable))](https://pypi.org/project/docstrange-api/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

**The official Python SDK for the Nanonets Document AI API** — Extract, classify, and analyze documents with state-of-the-art AI models.

## Features

- 🔍 **Document Extraction** — Convert PDFs, images, and documents to Markdown, HTML, JSON, or CSV
- 📊 **Document Classification** — Classify documents into custom categories with confidence scores
- 💬 **Chat Completions** — OpenAI-compatible chat API with vision capabilities
- ⚡ **Streaming Support** — Real-time Server-Sent Events (SSE) for progressive extraction
- 🔄 **Async & Sync Clients** — Both synchronous and async interfaces
- 📦 **Type-Safe** — Full type hints and Pydantic models for IDE autocomplete
- 🔁 **Auto-Retry** — Built-in retry logic with exponential backoff
- 📄 **Pagination** — Auto-paginating iterators for list endpoints

## Quick Start

### Installation

```bash
pip install docstrange-api
```

### Get Your API Key

1. Sign up at [nanonets.com](https://nanonets.com)
2. Navigate to **Settings** → **API Keys**
3. Create a new API key

### Basic Usage

```python
from docstrange import Docstrange

# Initialize the client
client = Docstrange(api_key="your-api-key")

# Extract content from a PDF
with open("document.pdf", "rb") as f:
    response = client.extract.sync(
        file=f,
        output_format="markdown",
    )

print(response.result.markdown.content)
```

## Documentation

| Resource | Description |
|----------|-------------|
| [API Reference](api.md) | Complete SDK method reference |
| [REST API Docs](https://docs.nanonets.com) | Full REST API documentation |
| [Examples](examples/) | Code examples for common use cases |

---

## Core Concepts

### Input Methods

The SDK supports three ways to provide documents:

```python
# 1. File upload (binary)
with open("document.pdf", "rb") as f:
    response = client.extract.sync(file=f, output_format="markdown")

# 2. Base64-encoded content
import base64
with open("document.pdf", "rb") as f:
    b64_content = base64.b64encode(f.read()).decode()
response = client.extract.sync(file_base64=b64_content, output_format="markdown")

# 3. URL (publicly accessible)
response = client.extract.sync(
    file_url="https://example.com/document.pdf",
    output_format="markdown",
)
```

### Output Formats

| Format | Description | Use Case |
|--------|-------------|----------|
| `markdown` | Structured Markdown with headers, lists, tables | LLM context, RAG pipelines |
| `html` | HTML with semantic tags | Web display |
| `json` | Structured key-value extraction | Form processing, data entry |
| `csv` | Tabular data extraction | Spreadsheet import, analytics |

```python
# Single format
response = client.extract.sync(file=f, output_format="markdown")
print(response.result.markdown.content)

# Multiple formats
response = client.extract.sync(file=f, output_format="markdown,json")
print(response.result.markdown.content)
print(response.result.json_.content)  # Note: json_ (reserved keyword)
```

---

## API Reference

### Document Extraction

#### Synchronous Extraction

Process a document and wait for the result:

```python
response = client.extract.sync(
    file=open("invoice.pdf", "rb"),
    output_format="json",
    json_options='["invoice_number", "date", "total", "vendor"]',
    custom_instructions="Extract all line items with quantities and prices",
)

print(f"Invoice #: {response.result.json_.content.get('invoice_number')}")
print(f"Total: {response.result.json_.content.get('total')}")
```

#### Asynchronous Extraction

Queue a document for processing and poll for results:

```python
# Submit for async processing
job = client.extract.async_(
    file_base64=base64_content,
    output_format="markdown",
)
print(f"Job queued: {job.record_id}")

# Poll for completion
import time
while True:
    result = client.extract.results.retrieve(job.record_id)
    if result.status == "completed":
        print(result.result.markdown.content)
        break
    elif result.status == "failed":
        print(f"Error: {result.message}")
        break
    time.sleep(2)
```

#### Streaming Extraction (SSE)

Get results progressively as they're generated:

```python
with client.extract.stream(
    file_base64=base64_content,
    output_format="markdown",
) as stream:
    for event in stream:
        if event.get("type") == "content":
            print(event["data"], end="", flush=True)
        elif event.get("type") == "done":
            print(f"\n\nCompleted in {event['processing_time']}s")
```

#### Batch Extraction

Process multiple files in parallel:

```python
files = [open("doc1.pdf", "rb"), open("doc2.pdf", "rb"), open("doc3.pdf", "rb")]

response = client.extract.batch(
    files=files,
    output_format="markdown",
)

print(f"Batch {response.batch_id}: {response.accepted_files}/{response.total_files} accepted")

for record in response.records:
    print(f"  {record.filename}: {record.status}")
```

### Extraction Options

#### JSON Schema Extraction

Extract structured data using predefined fields:

```python
# Simple field list
response = client.extract.sync(
    file=f,
    output_format="json",
    json_options='["name", "email", "phone", "address"]',
)

# With custom instructions
response = client.extract.sync(
    file=f,
    output_format="json",
    json_options='["invoice_number", "line_items", "subtotal", "tax", "total"]',
    custom_instructions="For line_items, extract as array with description, quantity, unit_price",
)
```

#### Include Metadata

Get additional information like bounding boxes and confidence scores:

```python
# Block-level bounding boxes
response = client.extract.sync(
    file=f,
    output_format="markdown",
    include_metadata="bounding_boxes",
)
boxes = response.result.markdown.metadata.bounding_boxes

# Word-level bounding boxes
response = client.extract.sync(
    file=f,
    output_format="markdown",
    include_metadata="bounding_boxes_word",
)

# Confidence scores (for JSON extraction)
response = client.extract.sync(
    file=f,
    output_format="json",
    include_metadata="confidence_score",
)
scores = response.result.json_.metadata.confidence_score
```

#### Custom Instructions

Guide the extraction with natural language:

```python
# Append to default prompt
response = client.extract.sync(
    file=f,
    output_format="markdown",
    custom_instructions="Focus on financial data. Format all currency as USD.",
    prompt_mode="append",
)

# Replace default prompt entirely
response = client.extract.sync(
    file=f,
    output_format="markdown",
    custom_instructions="Extract only the executive summary section.",
    prompt_mode="replace",
)
```

### Results Management

#### Retrieve a Result

```python
result = client.extract.results.retrieve("12345")
print(f"Status: {result.status}")
print(f"File: {result.filename}")
print(f"Processing time: {result.processing_time}s")

if result.status == "completed":
    print(result.result.markdown.content)
```

#### List All Results (Paginated)

```python
# Auto-paginating iterator
for result in client.extract.results.list(page_size=20):
    print(f"{result.record_id}: {result.filename} ({result.status})")

# Manual pagination
page = client.extract.results.list(page=1, page_size=10, sort_by="created_at", sort_order="desc")
print(f"Page {page.pagination.page} of {page.pagination.total_pages}")

for result in page.results:
    print(f"  {result.record_id}: {result.filename}")

if page.has_next_page():
    next_page = page.get_next_page()
```

---

### Document Classification

Classify documents into custom categories:

```python
categories = '''[
    {"name": "Invoice", "description": "Bills, invoices, and payment requests"},
    {"name": "Contract", "description": "Legal agreements and contracts"},
    {"name": "Resume", "description": "CVs and job applications"},
    {"name": "Report", "description": "Business reports and analysis"}
]'''

with open("document.pdf", "rb") as f:
    response = client.classify.sync(
        file=f,
        categories=categories,
    )

for page in response.result.pages:
    print(f"Page {page.page_number}: {page.category} ({page.confidence}%)")
    print(f"  Reasoning: {page.reasoning}")
```

#### Batch Classification

```python
files = [open("doc1.pdf", "rb"), open("doc2.pdf", "rb")]

response = client.classify.batch(
    files=files,
    categories=categories,
)

for result in response.results:
    print(f"{result.filename}: {result.pages[0].category}")
```

---

### Chat Completions (Vision)

OpenAI-compatible chat API with document understanding:

```python
# Text-only completion
response = client.chat.create_completion(
    model="nanonets/Nanonets-OCR-s",
    messages=[
        {"role": "user", "content": [
            {"type": "text", "text": "What is the capital of France?"}
        ]}
    ],
)

# Vision: analyze an image
response = client.chat.create_completion(
    model="nanonets/Nanonets-OCR-s",
    messages=[
        {"role": "user", "content": [
            {"type": "image_url", "image_url": {"url": "https://example.com/chart.png"}},
            {"type": "text", "text": "Describe this chart and extract the key data points."}
        ]}
    ],
)
```

---

## Async Client

For asyncio applications:

```python
import asyncio
from docstrange import AsyncDocstrange

async def main():
    client = AsyncDocstrange(api_key="your-api-key")
    
    response = await client.extract.sync(
        file_base64=base64_content,
        output_format="markdown",
    )
    print(response.result.markdown.content)
    
    # Don't forget to close
    await client.close()

asyncio.run(main())
```

Or use as context manager:

```python
async with AsyncDocstrange(api_key="your-api-key") as client:
    response = await client.extract.sync(
        file_base64=base64_content,
        output_format="markdown",
    )
```

### With aiohttp (Better Concurrency)

```python
from docstrange import AsyncDocstrange, DefaultAioHttpClient

# Install: pip install docstrange-api[aiohttp]

async with AsyncDocstrange(
    api_key="your-api-key",
    http_client=DefaultAioHttpClient(),
) as client:
    response = await client.extract.sync(...)
```

---

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DOCSTRANGE_API_KEY` | API key for authentication | Required |
| `DOCSTRANGE_BASE_URL` | API base URL | `https://extraction-api.nanonets.com` |
| `DOCSTRANGE_LOG` | Log level (`info`, `debug`) | None |

```python
import os
os.environ["DOCSTRANGE_API_KEY"] = "your-api-key"

# Client will auto-detect from environment
client = Docstrange()
```

### Client Options

```python
client = Docstrange(
    api_key="your-api-key",
    base_url="https://extraction-api.nanonets.com",  # Custom endpoint
    timeout=120.0,  # Request timeout in seconds (default: 60)
    max_retries=3,  # Retry attempts (default: 2)
)
```

### Per-Request Options

```python
# Override timeout for a specific request
response = client.with_options(timeout=300.0).extract.sync(
    file=large_file,
    output_format="markdown",
)
```

---

## Error Handling

```python
import docstrange
from docstrange import Docstrange

client = Docstrange()

try:
    response = client.extract.sync(file=f, output_format="markdown")
except docstrange.AuthenticationError:
    print("Invalid API key")
except docstrange.RateLimitError as e:
    print(f"Rate limited. Retry after: {e.response.headers.get('Retry-After')}s")
except docstrange.BadRequestError as e:
    print(f"Invalid request: {e.message}")
except docstrange.APIConnectionError:
    print("Network error - check your connection")
except docstrange.APIStatusError as e:
    print(f"API error {e.status_code}: {e.message}")
```

### Error Types

| Status Code | Exception | Description |
|-------------|-----------|-------------|
| 400 | `BadRequestError` | Invalid request parameters |
| 401 | `AuthenticationError` | Invalid or missing API key |
| 403 | `PermissionDeniedError` | Insufficient permissions |
| 404 | `NotFoundError` | Resource not found |
| 422 | `UnprocessableEntityError` | Validation error |
| 429 | `RateLimitError` | Rate limit exceeded |
| ≥500 | `InternalServerError` | Server error |
| N/A | `APIConnectionError` | Network connectivity issue |
| N/A | `APITimeoutError` | Request timed out |

---

## Advanced Usage

### Raw Response Access

```python
response = client.extract.with_raw_response.sync(
    file=f,
    output_format="markdown",
)

print(f"Status: {response.status_code}")
print(f"Headers: {response.headers}")

# Parse the body
result = response.parse()
print(result.result.markdown.content)
```

### Streaming Response

```python
with client.extract.with_streaming_response.sync(
    file=f,
    output_format="markdown",
) as response:
    for chunk in response.iter_bytes():
        process(chunk)
```

### Custom HTTP Client

```python
import httpx
from docstrange import Docstrange, DefaultHttpxClient

client = Docstrange(
    api_key="your-api-key",
    http_client=DefaultHttpxClient(
        proxy="http://proxy.example.com:8080",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

---

## Type Reference

### Response Models

```python
from docstrange.types import (
    # Extraction
    ExtractResponse,
    ExtractionResult,
    ExtractionFormatResult,
    ExtractionMetadata,
    BatchExtractResponse,
    
    # Classification
    ClassifyResponse,
    BatchClassifyResponse,
    FileClassificationResult,
    PageClassification,
    
    # Pagination
    ExtractionListResponse,
    PaginationInfo,
)
```

### Response Structure

```python
ExtractResponse:
    success: bool
    message: str
    record_id: str
    status: str  # "completed", "processing", "failed"
    result: ExtractionResult | None
    processing_time: float | None
    filename: str | None
    output_format: str | None
    file_size: int | None
    pages_processed: int | None
    created_at: str | None
    signed_url: str | None  # Download URL for original file

ExtractionResult:
    markdown: ExtractionFormatResult | None
    html: ExtractionFormatResult | None
    json_: ExtractionFormatResult | None  # Note: json_ not json
    csv: ExtractionFormatResult | None

ExtractionFormatResult:
    content: str | dict | list
    metadata: ExtractionMetadata

ExtractionMetadata:
    bounding_boxes: dict | None
    confidence_score: dict | None
```

---

## Requirements

- Python 3.9+
- Dependencies: `httpx`, `pydantic`, `typing-extensions`, `anyio`, `distro`

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and guidelines.

## License

Apache 2.0 - See [LICENSE](LICENSE) for details.

## Support

- 📚 [Documentation](https://docs.nanonets.com)
- 🐛 [Issue Tracker](https://github.com/NanoNets/docstrange-python/issues)
- 💬 [Discord Community](https://discord.gg/nanonets)
- 📧 [Email Support](mailto:support@nanonets.com)
