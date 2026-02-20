#!/usr/bin/env python3
"""
Structured JSON Extraction Example

This example demonstrates how to extract specific fields from documents
as structured JSON data.

Usage:
    export DOCSTRANGE_API_KEY="your-api-key"
    python json_extraction.py invoice.pdf
"""

import json
import sys
from pathlib import Path

from docstrange import Docstrange


def extract_invoice(file_path: Path) -> dict:
    """Extract invoice data with specific fields."""
    client = Docstrange()

    # Define fields to extract
    fields = [
        "invoice_number",
        "invoice_date",
        "due_date",
        "vendor_name",
        "vendor_address",
        "customer_name",
        "customer_address",
        "line_items",
        "subtotal",
        "tax",
        "total",
    ]

    with open(file_path, "rb") as f:
        response = client.extract.sync(
            file=f,
            output_format="json",
            json_options=json.dumps(fields),
            custom_instructions="""
                For line_items, extract as an array with:
                - description: item description
                - quantity: number of items
                - unit_price: price per item
                - amount: total for this line
                
                Format all dates as YYYY-MM-DD.
                Format all currency values as numbers without symbols.
            """,
        )

    if response.success:
        return response.result.json_.content
    else:
        raise Exception(f"Extraction failed: {response.message}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python json_extraction.py <invoice_pdf>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    print(f"Extracting structured data from: {file_path.name}")
    print("-" * 50)

    try:
        data = extract_invoice(file_path)
        
        # Pretty print the extracted data
        print(json.dumps(data, indent=2))
        
        # Example: Access specific fields
        print("\n" + "=" * 50)
        print("SUMMARY:")
        print("=" * 50)
        print(f"Invoice #: {data.get('invoice_number', 'N/A')}")
        print(f"Vendor: {data.get('vendor_name', 'N/A')}")
        print(f"Total: ${data.get('total', 'N/A')}")
        
        # Line items
        line_items = data.get("line_items", [])
        if line_items:
            print(f"\nLine Items ({len(line_items)}):")
            for i, item in enumerate(line_items, 1):
                if isinstance(item, dict):
                    desc = item.get("description", "Unknown")
                    qty = item.get("quantity", "?")
                    price = item.get("unit_price", "?")
                    print(f"  {i}. {desc} - Qty: {qty} @ ${price}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
