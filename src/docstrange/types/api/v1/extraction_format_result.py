# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional

from ...._models import BaseModel

__all__ = ["ExtractionFormatResult", "Metadata"]


class Metadata(BaseModel):
    bounding_boxes: Optional[object] = None
    """Element coordinates with page dimensions"""

    confidence_score: Optional[object] = None
    """Confidence scores per field"""


class ExtractionFormatResult(BaseModel):
    content: Union[str, object]
    """Extracted content"""

    metadata: Optional[Metadata] = None
