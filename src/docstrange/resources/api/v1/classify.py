# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ...._types import (
    Body,
    Query,
    Headers,
    NotGiven,
    FileTypes,
    SequenceNotStr,
    not_given,
)
from ...._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.api.v1 import classify_sync_params, classify_batch_params
from ....types.api.v1.classify_sync_response import ClassifySyncResponse
from ....types.api.v1.classify_batch_response import ClassifyBatchResponse

__all__ = ["ClassifyResource", "AsyncClassifyResource"]


class ClassifyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClassifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/docstrange-python#accessing-raw-response-data-eg-headers
        """
        return ClassifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/docstrange-python#with_streaming_response
        """
        return ClassifyResourceWithStreamingResponse(self)

    def batch(
        self,
        *,
        categories: str,
        files: SequenceNotStr[FileTypes],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyBatchResponse:
        """
        Classify multiple documents asynchronously (max 50 files).

        Files are queued for background processing. Use
        `GET /api/v1/extract/results/{record_id}` to poll results.

        Args:
          categories: JSON array of category objects (max 50 categories)

          files: Files to classify (max 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "categories": categories,
                "files": files,
            }
        )
        extracted_files = extract_files(cast(Mapping[str, object], body), paths=[["files", "<array>"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/classify/batch",
            body=maybe_transform(body, classify_batch_params.ClassifyBatchParams),
            files=extracted_files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifyBatchResponse,
        )

    def sync(
        self,
        *,
        categories: str,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifySyncResponse:
        """
        Classify a single document into predefined categories synchronously.

        Each page is classified individually with category, confidence score (0-100),
        and reasoning.

        Args:
          categories:
              JSON array of category objects: [{"name": "Category Name", "description":
              "Optional description"}]

          file: File to classify (PDF, PNG, JPG, JPEG, TIFF, BMP, WebP)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "categories": categories,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/classify/sync",
            body=maybe_transform(body, classify_sync_params.ClassifySyncParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifySyncResponse,
        )


class AsyncClassifyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClassifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/docstrange-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClassifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/docstrange-python#with_streaming_response
        """
        return AsyncClassifyResourceWithStreamingResponse(self)

    async def batch(
        self,
        *,
        categories: str,
        files: SequenceNotStr[FileTypes],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyBatchResponse:
        """
        Classify multiple documents asynchronously (max 50 files).

        Files are queued for background processing. Use
        `GET /api/v1/extract/results/{record_id}` to poll results.

        Args:
          categories: JSON array of category objects (max 50 categories)

          files: Files to classify (max 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "categories": categories,
                "files": files,
            }
        )
        extracted_files = extract_files(cast(Mapping[str, object], body), paths=[["files", "<array>"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/classify/batch",
            body=await async_maybe_transform(body, classify_batch_params.ClassifyBatchParams),
            files=extracted_files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifyBatchResponse,
        )

    async def sync(
        self,
        *,
        categories: str,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifySyncResponse:
        """
        Classify a single document into predefined categories synchronously.

        Each page is classified individually with category, confidence score (0-100),
        and reasoning.

        Args:
          categories:
              JSON array of category objects: [{"name": "Category Name", "description":
              "Optional description"}]

          file: File to classify (PDF, PNG, JPG, JPEG, TIFF, BMP, WebP)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "categories": categories,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/classify/sync",
            body=await async_maybe_transform(body, classify_sync_params.ClassifySyncParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifySyncResponse,
        )


class ClassifyResourceWithRawResponse:
    def __init__(self, classify: ClassifyResource) -> None:
        self._classify = classify

        self.batch = to_raw_response_wrapper(
            classify.batch,
        )
        self.sync = to_raw_response_wrapper(
            classify.sync,
        )


class AsyncClassifyResourceWithRawResponse:
    def __init__(self, classify: AsyncClassifyResource) -> None:
        self._classify = classify

        self.batch = async_to_raw_response_wrapper(
            classify.batch,
        )
        self.sync = async_to_raw_response_wrapper(
            classify.sync,
        )


class ClassifyResourceWithStreamingResponse:
    def __init__(self, classify: ClassifyResource) -> None:
        self._classify = classify

        self.batch = to_streamed_response_wrapper(
            classify.batch,
        )
        self.sync = to_streamed_response_wrapper(
            classify.sync,
        )


class AsyncClassifyResourceWithStreamingResponse:
    def __init__(self, classify: AsyncClassifyResource) -> None:
        self._classify = classify

        self.batch = async_to_streamed_response_wrapper(
            classify.batch,
        )
        self.sync = async_to_streamed_response_wrapper(
            classify.sync,
        )
