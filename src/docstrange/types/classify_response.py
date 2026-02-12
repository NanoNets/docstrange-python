# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .file_classification_result import FileClassificationResult

__all__ = ["ClassifyResponse"]


class ClassifyResponse(BaseModel):
    message: str

    success: bool

    result: Optional[FileClassificationResult] = None
