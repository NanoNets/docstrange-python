# Docstrange Python SDK — API Reference

This document provides a complete reference for all SDK methods, types, and parameters.

---

## Table of Contents

- [Extract](#extract)
  - [Methods](#extract-methods)
  - [Results](#results)
- [Classify](#classify)
  - [Methods](#classify-methods)
- [Chat](#chat)
  - [Methods](#chat-methods)
- [Types Reference](#types-reference)

---

# Extract

Document extraction API for converting documents to structured formats.

## Types

```python
from docstrange.types import (
    ExtractResponse,           # Response from extraction endpoints
    ExtractionResult,          # Container for format-specific results
    ExtractionFormatResult,    # Single format result with content and metadata
    ExtractionMetadata,        # Bounding boxes and confidence scores
    BatchExtractResponse,      # Response from batch extraction
    ExtractStreamResponse,     # Streaming event types
)
```

## Extract Methods

### `client.extract.sync(**params) -> ExtractResponse`

**Synchronous extraction** — Process a document and wait for results.

```python
response = client.extract.sync(
    file=open("doc.pdf", "rb"),        # Binary file (mutually exclusive with below)
    file_base64="...",                  # Base64-encoded file content
    file_url="https://...",             # Publicly accessible URL
    output_format="markdown",           # Required: markdown, html, json, csv (comma-separated)
    json_options='["field1", "field2"]', # Optional: fields for JSON extraction
    csv_options="table",                # Optional: CSV extraction mode
    markdown_options="financial-docs",  # Optional: Markdown extraction mode
    include_metadata="bounding_boxes",  # Optional: bounding_boxes, bounding_boxes_word, confidence_score
    custom_instructions="...",          # Optional: Natural language guidance
    prompt_mode="append",               # Optional: append (default) or replace
    model_type="nanonets-ocr-2.1",      # Optional: Model selection
)
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file` | `BinaryIO` | One of three | File upload (binary mode) |
| `file_base64` | `str` | One of three | Base64-encoded file content |
| `file_url` | `str` | One of three | URL to download file from |
| `output_format` | `str` | ✅ | Output formats: `markdown`, `html`, `json`, `csv` (comma-separated for multiple) |
| `json_options` | `str` | ❌ | JSON array of field names, or `"hierarchy_output"`, `"table-of-contents"` |
| `csv_options` | `str` | ❌ | `"table"` for table extraction, `"toc"` for table of contents |
| `markdown_options` | `str` | ❌ | `"financial-docs"` for financial formatting, `"toc"` for TOC |
| `include_metadata` | `str` | ❌ | Comma-separated: `bounding_boxes`, `bounding_boxes_word`, `confidence_score` |
| `custom_instructions` | `str` | ❌ | Natural language extraction guidance (max 8000 chars) |
| `prompt_mode` | `str` | ❌ | `"append"` (default) or `"replace"` |
| `model_type` | `str` | ❌ | `""` (default model) or `"nanonets-ocr-2.1"` |

**Returns:** `ExtractResponse`

---

### `client.extract.async_(**params) -> ExtractResponse`

**Asynchronous extraction** — Queue a document and get a record_id for polling.

```python
response = client.extract.async_(
    file_base64=base64_content,
    output_format="markdown",
)
# response.record_id can be used with client.extract.results.retrieve()
```

Parameters are identical to `sync()`.

**Returns:** `ExtractResponse` with `status="processing"` or `status="queued"`

---

### `client.extract.stream(**params) -> Stream`

**Streaming extraction** — Get results via Server-Sent Events as they're generated.

```python
with client.extract.stream(
    file_base64=base64_content,
    output_format="markdown",
    enable_streaming=True,  # Default: True
) as stream:
    for event in stream:
        print(event)
```

Additional parameter:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `enable_streaming` | `bool` | ❌ | `True` for chunk-by-chunk, `False` for batch mode |

**Event Types:**
- `{"type": "metadata", "model": "...", "streaming_mode": "streaming"}`
- `{"type": "content", "data": "..."}`
- `{"type": "progress", "progress": 0.5, "message": "..."}`
- `{"type": "complete", "data": "..."}` (batch mode only)
- `{"type": "done", "record_id": "...", "processing_time": 2.5}`
- `{"type": "error", "error": "..."}`
- `{"type": "async_queued", "record_id": "...", "total_pages": 10, "message": "..."}`

---

### `client.extract.batch(**params) -> BatchExtractResponse`

**Batch extraction** — Process multiple files (max 50).

```python
response = client.extract.batch(
    files=[open("doc1.pdf", "rb"), open("doc2.pdf", "rb")],
    output_format="markdown",
)
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `files` | `List[BinaryIO]` | ✅ | List of files (max 50) |
| `output_format` | `str` | ✅ | Output format(s) |
| *(other params)* | | | Same as `sync()` |

**Returns:** `BatchExtractResponse`

---

## Results

Methods for retrieving extraction results.

### Types

```python
from docstrange.types.extract import ExtractionListResponse, PaginationInfo
```

### `client.extract.results.retrieve(record_id, **params) -> ExtractResponse`

**Get extraction result** by record ID.

```python
result = client.extract.results.retrieve(
    record_id="12345",
    include_content=True,  # Optional: include full content (default: True)
)
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `record_id` | `str` | ✅ | The record ID from extraction response |
| `include_content` | `bool` | ❌ | Whether to include full content |

**Returns:** `ExtractResponse`

---

### `client.extract.results.list(**params) -> SyncPageNumberPagination[ExtractResponse]`

**List all extraction results** for the authenticated user.

```python
# Auto-paginating iterator
for result in client.extract.results.list():
    print(result.record_id, result.filename)

# Manual pagination
page = client.extract.results.list(
    page=1,
    page_size=20,
    sort_by="created_at",
    sort_order="desc",
)
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `page` | `int` | ❌ | Page number (1-based, default: 1) |
| `page_size` | `int` | ❌ | Items per page (1-100, default: 20) |
| `sort_by` | `str` | ❌ | Sort field: `created_at`, `updated_at`, `original_filename`, `file_size`, `processing_status`, `output_type` |
| `sort_order` | `str` | ❌ | `"asc"` or `"desc"` (default: `"desc"`) |

**Returns:** `SyncPageNumberPagination[ExtractResponse]`

**Pagination Methods:**
- `.has_next_page() -> bool`
- `.next_page_info() -> PageInfo`
- `.get_next_page() -> SyncPageNumberPagination`
- `.iter_pages() -> Iterator`

---

# Classify

Document classification API for categorizing documents.

## Types

```python
from docstrange.types import (
    ClassifyResponse,           # Response from classification
    BatchClassifyResponse,      # Response from batch classification
    FileClassificationResult,   # Classification result for a file
    PageClassification,         # Classification for a single page
)
```

## Classify Methods

### `client.classify.sync(**params) -> ClassifyResponse`

**Classify a document** into custom categories.

```python
response = client.classify.sync(
    file=open("document.pdf", "rb"),
    categories='[{"name": "Invoice", "description": "Bills and invoices"}, {"name": "Contract", "description": "Legal agreements"}]',
)

for page in response.result.pages:
    print(f"Page {page.page_number}: {page.category} ({page.confidence}%)")
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file` | `BinaryIO` | ✅ | File to classify |
| `categories` | `str` | ✅ | JSON array of `{"name": "...", "description": "..."}` (max 50) |

**Returns:** `ClassifyResponse`

---

### `client.classify.batch(**params) -> BatchClassifyResponse`

**Batch classify** multiple documents.

```python
response = client.classify.batch(
    files=[open("doc1.pdf", "rb"), open("doc2.pdf", "rb")],
    categories='[{"name": "Invoice"}, {"name": "Contract"}]',
)
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `files` | `List[BinaryIO]` | ✅ | List of files |
| `categories` | `str` | ✅ | JSON array of categories |

**Returns:** `BatchClassifyResponse`

---

# Chat

OpenAI-compatible chat completions API with vision capabilities.

## Types

```python
from docstrange.types import ChatCompletionsRequest
```

## Chat Methods

### `client.chat.create_completion(**params) -> object`

**Create a chat completion** with optional vision input.

```python
# Text-only
response = client.chat.create_completion(
    model="nanonets/Nanonets-OCR-s",
    messages=[
        {"role": "user", "content": [
            {"type": "text", "text": "Hello!"}
        ]}
    ],
)

# With image
response = client.chat.create_completion(
    model="nanonets/Nanonets-OCR-s",
    messages=[
        {"role": "user", "content": [
            {"type": "image_url", "image_url": {"url": "https://..."}},
            {"type": "text", "text": "Describe this image."}
        ]}
    ],
)
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `model` | `str` | ✅ | Model identifier (e.g., `"nanonets/Nanonets-OCR-s"`) |
| `messages` | `List[Message]` | ✅ | Chat messages array |

**Message Format:**
```python
{
    "role": "user" | "assistant" | "system",
    "content": [
        {"type": "text", "text": "..."},
        {"type": "image_url", "image_url": {"url": "https://..."}}
    ]
}
```

**Returns:** Chat completion response object

---

# Types Reference

## ExtractResponse

```python
class ExtractResponse:
    success: bool                           # Whether extraction succeeded
    message: str                            # Status message
    record_id: str                          # Unique extraction ID
    status: str                             # "completed", "processing", "queued", "failed"
    result: Optional[ExtractionResult]      # Extraction results (None if processing)
    processing_time: Optional[float]        # Time in seconds
    filename: Optional[str]                 # Original filename
    output_format: Optional[str]            # Requested format(s)
    file_size: Optional[int]                # File size in bytes
    pages_processed: Optional[int]          # Number of pages processed
    created_at: Optional[str]               # ISO 8601 timestamp
    signed_url: Optional[str]               # Download URL for original file
    request_config: Optional[RequestConfig] # Original request parameters
```

## ExtractionResult

```python
class ExtractionResult:
    markdown: Optional[ExtractionFormatResult]  # Markdown result
    html: Optional[ExtractionFormatResult]      # HTML result
    json_: Optional[ExtractionFormatResult]     # JSON result (note: json_ not json)
    csv: Optional[ExtractionFormatResult]       # CSV result
```

## ExtractionFormatResult

```python
class ExtractionFormatResult:
    content: Union[str, dict, list]         # Extracted content
    metadata: ExtractionMetadata            # Associated metadata
```

## ExtractionMetadata

```python
class ExtractionMetadata:
    bounding_boxes: Optional[dict]          # Block/word coordinates
    confidence_score: Optional[dict]        # Field confidence scores
```

## BatchExtractResponse

```python
class BatchExtractResponse:
    success: bool
    message: str
    batch_id: str
    total_files: int
    accepted_files: int
    rejected_files: int
    records: List[ExtractResponse]
```

## ClassifyResponse

```python
class ClassifyResponse:
    success: bool
    message: str
    result: Optional[FileClassificationResult]
```

## FileClassificationResult

```python
class FileClassificationResult:
    filename: str
    record_id: Optional[str]
    total_pages: int
    pages: List[PageClassification]
    processing_time: Optional[float]
    error: Optional[str]
```

## PageClassification

```python
class PageClassification:
    page_number: int           # 1-indexed
    category: str              # Matched category name
    confidence: int            # 0-100
    reasoning: str             # Explanation
    identified_category: Optional[str]  # Original if "Other"
```

## PaginationInfo

```python
class PaginationInfo:
    page: int
    page_size: int
    total_count: int
    total_pages: int
    has_next: bool
    has_previous: bool
```
