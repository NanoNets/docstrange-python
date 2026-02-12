# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .extraction_metadata import ExtractionMetadata

__all__ = ["ExtractionFormatResult"]


class ExtractionFormatResult(BaseModel):
    content: object
    """Extracted content (string or object)"""

    metadata: Optional[ExtractionMetadata] = None
