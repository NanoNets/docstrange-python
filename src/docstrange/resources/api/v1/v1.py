# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .classify import (
    ClassifyResource,
    AsyncClassifyResource,
    ClassifyResourceWithRawResponse,
    AsyncClassifyResourceWithRawResponse,
    ClassifyResourceWithStreamingResponse,
    AsyncClassifyResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .extract.extract import (
    ExtractResource,
    AsyncExtractResource,
    ExtractResourceWithRawResponse,
    AsyncExtractResourceWithRawResponse,
    ExtractResourceWithStreamingResponse,
    AsyncExtractResourceWithStreamingResponse,
)

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def extract(self) -> ExtractResource:
        return ExtractResource(self._client)

    @cached_property
    def classify(self) -> ClassifyResource:
        return ClassifyResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/docstrange-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/docstrange-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def extract(self) -> AsyncExtractResource:
        return AsyncExtractResource(self._client)

    @cached_property
    def classify(self) -> AsyncClassifyResource:
        return AsyncClassifyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/docstrange-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/docstrange-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def extract(self) -> ExtractResourceWithRawResponse:
        return ExtractResourceWithRawResponse(self._v1.extract)

    @cached_property
    def classify(self) -> ClassifyResourceWithRawResponse:
        return ClassifyResourceWithRawResponse(self._v1.classify)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def extract(self) -> AsyncExtractResourceWithRawResponse:
        return AsyncExtractResourceWithRawResponse(self._v1.extract)

    @cached_property
    def classify(self) -> AsyncClassifyResourceWithRawResponse:
        return AsyncClassifyResourceWithRawResponse(self._v1.classify)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def extract(self) -> ExtractResourceWithStreamingResponse:
        return ExtractResourceWithStreamingResponse(self._v1.extract)

    @cached_property
    def classify(self) -> ClassifyResourceWithStreamingResponse:
        return ClassifyResourceWithStreamingResponse(self._v1.classify)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def extract(self) -> AsyncExtractResourceWithStreamingResponse:
        return AsyncExtractResourceWithStreamingResponse(self._v1.extract)

    @cached_property
    def classify(self) -> AsyncClassifyResourceWithStreamingResponse:
        return AsyncClassifyResourceWithStreamingResponse(self._v1.classify)
