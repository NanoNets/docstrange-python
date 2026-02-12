# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional

from .._models import BaseModel
from .extraction_metadata import ExtractionMetadata

__all__ = ["ExtractionFormatResult"]


class ExtractionFormatResult(BaseModel):
    content: Union[str, object]
    """Extracted content"""

    metadata: Optional[ExtractionMetadata] = None
