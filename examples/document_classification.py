#!/usr/bin/env python3
"""
Document Classification Example

This example demonstrates how to classify documents into custom categories.

Usage:
    export DOCSTRANGE_API_KEY="your-api-key"
    python document_classification.py document.pdf
"""

import json
import sys
from pathlib import Path

from docstrange import Docstrange


def main():
    if len(sys.argv) < 2:
        print("Usage: python document_classification.py <file_path>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    client = Docstrange()

    # Define classification categories
    categories = [
        {
            "name": "Invoice",
            "description": "Bills, invoices, payment requests, and receipts"
        },
        {
            "name": "Contract",
            "description": "Legal agreements, contracts, terms of service"
        },
        {
            "name": "Resume",
            "description": "CVs, resumes, job applications"
        },
        {
            "name": "Report",
            "description": "Business reports, analysis documents, presentations"
        },
        {
            "name": "Letter",
            "description": "Business letters, correspondence, memos"
        },
        {
            "name": "Form",
            "description": "Application forms, government forms, questionnaires"
        },
    ]

    print(f"Classifying: {file_path.name}")
    print(f"Categories: {', '.join(c['name'] for c in categories)}")
    print("-" * 50)

    with open(file_path, "rb") as f:
        response = client.classify.sync(
            file=f,
            categories=json.dumps(categories),
        )

    if response.success and response.result:
        result = response.result
        print(f"\n✓ Classification completed")
        print(f"  File: {result.filename}")
        print(f"  Total pages: {result.total_pages}")
        print(f"  Processing time: {result.processing_time:.2f}s")
        print()

        print("PAGE-BY-PAGE CLASSIFICATION:")
        print("=" * 50)

        for page in result.pages:
            confidence_bar = "█" * (page.confidence // 10) + "░" * (10 - page.confidence // 10)
            print(f"\nPage {page.page_number}:")
            print(f"  Category:   {page.category}")
            print(f"  Confidence: [{confidence_bar}] {page.confidence}%")
            print(f"  Reasoning:  {page.reasoning}")

            if page.identified_category:
                print(f"  Note: Model identified as '{page.identified_category}' but categorized as 'Other'")

        # Summary
        print("\n" + "=" * 50)
        print("SUMMARY:")
        
        # Count pages per category
        category_counts = {}
        for page in result.pages:
            cat = page.category
            category_counts[cat] = category_counts.get(cat, 0) + 1

        for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
            print(f"  {cat}: {count} page(s)")

    else:
        print(f"✗ Classification failed: {response.message}")
        sys.exit(1)


if __name__ == "__main__":
    main()
