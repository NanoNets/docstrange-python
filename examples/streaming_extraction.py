#!/usr/bin/env python3
"""
Streaming Extraction Example

This example demonstrates real-time streaming extraction using Server-Sent Events.
Content is displayed progressively as it's generated.

Usage:
    export DOCSTRANGE_API_KEY="your-api-key"
    python streaming_extraction.py document.pdf
"""

import base64
import sys
from pathlib import Path

from docstrange import Docstrange


def main():
    if len(sys.argv) < 2:
        print("Usage: python streaming_extraction.py <file_path>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    client = Docstrange()

    # Read file as base64 (required for streaming)
    with open(file_path, "rb") as f:
        file_base64 = base64.b64encode(f.read()).decode("utf-8")

    print(f"Streaming extraction from: {file_path.name}")
    print("=" * 50)
    print()

    # Stream the extraction
    with client.extract.stream(
        file_base64=file_base64,
        output_format="markdown",
        enable_streaming=True,
    ) as stream:
        record_id = None
        processing_time = None

        for event in stream:
            event_type = event.get("type")

            if event_type == "metadata":
                model = event.get("model", "unknown")
                mode = event.get("streaming_mode", "streaming")
                print(f"[Model: {model}, Mode: {mode}]")
                print("-" * 50)

            elif event_type == "content":
                # Print content as it arrives
                print(event.get("data", ""), end="", flush=True)

            elif event_type == "progress":
                progress = event.get("progress", 0)
                message = event.get("message", "")
                # Progress updates (optional to display)
                pass

            elif event_type == "complete":
                # Batch mode: full content at once
                print(event.get("data", ""))

            elif event_type == "done":
                record_id = event.get("record_id")
                processing_time = event.get("processing_time")

            elif event_type == "error":
                print(f"\n\nError: {event.get('error')}")
                sys.exit(1)

            elif event_type == "async_queued":
                # Large file queued for async processing
                record_id = event.get("record_id")
                pages = event.get("total_pages")
                print(f"\nLarge document ({pages} pages) queued for async processing.")
                print(f"Record ID: {record_id}")
                print("Use client.extract.results.retrieve() to check status.")

    print()
    print("=" * 50)
    if record_id:
        print(f"Record ID: {record_id}")
    if processing_time:
        print(f"Processing time: {processing_time:.2f}s")


if __name__ == "__main__":
    main()
