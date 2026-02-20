# Docstrange Python SDK Examples

This directory contains practical examples demonstrating common use cases for the Docstrange Python SDK.

## Prerequisites

1. Install the SDK:
   ```bash
   pip install docstrange-api
   ```

2. Set your API key:
   ```bash
   export DOCSTRANGE_API_KEY="your-api-key"
   ```

## Examples

### Basic Extraction
**File:** `basic_extraction.py`

The simplest way to extract content from a document as Markdown.

```bash
python basic_extraction.py invoice.pdf
```

### JSON Extraction
**File:** `json_extraction.py`

Extract structured data with specific fields from invoices or forms.

```bash
python json_extraction.py invoice.pdf
```

### Streaming Extraction
**File:** `streaming_extraction.py`

Real-time extraction using Server-Sent Events. Content is displayed progressively as it's generated.

```bash
python streaming_extraction.py large_document.pdf
```

### Async with Polling
**File:** `async_with_polling.py`

Submit a document for async processing and poll for completion. Useful for large documents.

```bash
python async_with_polling.py large_document.pdf
```

### Document Classification
**File:** `document_classification.py`

Classify documents into custom categories with confidence scores.

```bash
python document_classification.py unknown_document.pdf
```

## Running All Examples

```bash
# Make examples executable
chmod +x *.py

# Run with a test document
./basic_extraction.py test.pdf
./json_extraction.py invoice.pdf
./streaming_extraction.py document.pdf
./document_classification.py document.pdf
./async_with_polling.py large_doc.pdf
```

## Tips

- **Input methods**: Examples use `file=` (binary), `file_base64=`, or `file_url=` depending on use case
- **Multiple formats**: Request multiple outputs with `output_format="markdown,json"`
- **Metadata**: Add `include_metadata="bounding_boxes"` for coordinate data
- **Custom extraction**: Use `custom_instructions` for specific extraction requirements
