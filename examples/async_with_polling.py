#!/usr/bin/env python3
"""
Async Extraction with Polling Example

This example demonstrates asynchronous document processing with polling.
Useful for large documents that take longer to process.

Usage:
    export DOCSTRANGE_API_KEY="your-api-key"
    python async_with_polling.py document.pdf
"""

import base64
import sys
import time
from pathlib import Path

from docstrange import Docstrange


def poll_until_complete(client: Docstrange, record_id: str, timeout: int = 120):
    """Poll for extraction completion with timeout."""
    start_time = time.time()
    poll_interval = 2  # seconds

    while time.time() - start_time < timeout:
        result = client.extract.results.retrieve(record_id)

        if result.status == "completed":
            return result
        elif result.status == "failed":
            raise Exception(f"Extraction failed: {result.message}")

        # Show progress
        elapsed = int(time.time() - start_time)
        print(f"  Status: {result.status} (elapsed: {elapsed}s)", end="\r")

        time.sleep(poll_interval)

    raise TimeoutError(f"Extraction did not complete within {timeout} seconds")


def main():
    if len(sys.argv) < 2:
        print("Usage: python async_with_polling.py <file_path>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    client = Docstrange()

    # Read file as base64
    with open(file_path, "rb") as f:
        file_base64 = base64.b64encode(f.read()).decode("utf-8")

    print(f"Submitting for async processing: {file_path.name}")
    print("-" * 50)

    # Submit for async processing
    job = client.extract.async_(
        file_base64=file_base64,
        output_format="markdown,json",  # Multiple formats
    )

    print(f"✓ Job submitted")
    print(f"  Record ID: {job.record_id}")
    print(f"  Status: {job.status}")
    print()
    print("Polling for completion...")

    try:
        result = poll_until_complete(client, job.record_id, timeout=120)
        print()  # Clear the status line
        print(f"\n✓ Extraction completed in {result.processing_time:.2f}s")
        print(f"  Pages processed: {result.pages_processed}")

        # Show results
        print("\n" + "=" * 50)
        print("MARKDOWN RESULT (first 500 chars):")
        print("=" * 50)
        markdown = result.result.markdown.content
        print(markdown[:500] + ("..." if len(markdown) > 500 else ""))

        print("\n" + "=" * 50)
        print("JSON RESULT:")
        print("=" * 50)
        import json
        print(json.dumps(result.result.json_.content, indent=2)[:1000])

    except TimeoutError as e:
        print(f"\n✗ {e}")
        print(f"You can check the status later with record_id: {job.record_id}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
