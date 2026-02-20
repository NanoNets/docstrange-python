#!/usr/bin/env python3
"""
Basic Document Extraction Example

This example demonstrates the simplest way to extract content from a document
using the Docstrange Python SDK.

Usage:
    export DOCSTRANGE_API_KEY="your-api-key"
    python basic_extraction.py document.pdf
"""

import sys
from pathlib import Path

from docstrange import Docstrange


def main():
    if len(sys.argv) < 2:
        print("Usage: python basic_extraction.py <file_path>")
        print("Example: python basic_extraction.py invoice.pdf")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    # Initialize the client (reads DOCSTRANGE_API_KEY from environment)
    client = Docstrange()

    print(f"Extracting content from: {file_path.name}")
    print("-" * 50)

    # Extract content as Markdown
    with open(file_path, "rb") as f:
        response = client.extract.sync(
            file=f,
            output_format="markdown",
        )

    if response.success:
        print(f"✓ Extraction completed in {response.processing_time:.2f}s")
        print(f"  Record ID: {response.record_id}")
        print(f"  Pages processed: {response.pages_processed}")
        print()
        print("=" * 50)
        print("EXTRACTED CONTENT:")
        print("=" * 50)
        print(response.result.markdown.content)
    else:
        print(f"✗ Extraction failed: {response.message}")
        sys.exit(1)


if __name__ == "__main__":
    main()
