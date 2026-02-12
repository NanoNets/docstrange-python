# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import extract_sync_params, extract_async_params, extract_batch_params, extract_stream_params
from .results import (
    ResultsResource,
    AsyncResultsResource,
    ResultsResourceWithRawResponse,
    AsyncResultsResourceWithRawResponse,
    ResultsResourceWithStreamingResponse,
    AsyncResultsResourceWithStreamingResponse,
)
from ..._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    FileTypes,
    SequenceNotStr,
    omit,
    not_given,
)
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ..._base_client import make_request_options
from ...types.extract_response import ExtractResponse
from ...types.batch_extract_response import BatchExtractResponse
from ...types.extract_stream_response import ExtractStreamResponse

__all__ = ["ExtractResource", "AsyncExtractResource"]


class ExtractResource(SyncAPIResource):
    @cached_property
    def results(self) -> ResultsResource:
        return ResultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NanoNets/docstrange-python#accessing-raw-response-data-eg-headers
        """
        return ExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NanoNets/docstrange-python#with_streaming_response
        """
        return ExtractResourceWithStreamingResponse(self)

    def async_(
        self,
        *,
        file: FileTypes,
        output_format: str,
        csv_options: str | Omit = omit,
        custom_instructions: str | Omit = omit,
        file_base64: str | Omit = omit,
        file_url: str | Omit = omit,
        include_metadata: str | Omit = omit,
        json_options: str | Omit = omit,
        prompt_mode: Literal["append", "replace"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractResponse:
        """Queue a document for background processing.

        Returns a `record_id` to poll
        results via `GET /api/v1/extract/results/{record_id}`.

        Recommended for large documents (>50 pages).

        Args:
          file: File to upload (PDF, Word, Excel, PowerPoint, images)

          output_format: Output format(s): `markdown`, `html`, `json`, `csv`. Comma-separate for multiple
              (e.g., `markdown,json`).

          csv_options: CSV extraction options (e.g., `table`)

          custom_instructions: Custom extraction instructions (e.g., `Format dates as YYYY-MM-DD`)

          file_base64: Base64-encoded file content

          file_url: URL to download file from

          include_metadata: Comma-separated metadata: `bounding_boxes`, `confidence_score`

          json_options: JSON extraction options. Values: `hierarchy_output`, `table-of-contents`, field
              list `["field1", "field2"]`, or JSON schema `{...}`

          prompt_mode: `append`: add to base prompt, `replace`: use only custom instructions

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/extract/async",
            body=maybe_transform(
                {
                    "file": file,
                    "output_format": output_format,
                    "csv_options": csv_options,
                    "custom_instructions": custom_instructions,
                    "file_base64": file_base64,
                    "file_url": file_url,
                    "include_metadata": include_metadata,
                    "json_options": json_options,
                    "prompt_mode": prompt_mode,
                },
                extract_async_params.ExtractAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    def batch(
        self,
        *,
        files: SequenceNotStr[FileTypes],
        output_format: str,
        csv_options: str | Omit = omit,
        custom_instructions: str | Omit = omit,
        include_metadata: str | Omit = omit,
        json_options: str | Omit = omit,
        prompt_mode: Literal["append", "replace"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchExtractResponse:
        """Process multiple files asynchronously (max 50 files).

        All files share the same
        extraction options.

        Args:
          files: Files to process (max 50)

          output_format: Output format(s) for all files

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/extract/batch",
            body=maybe_transform(
                {
                    "files": files,
                    "output_format": output_format,
                    "csv_options": csv_options,
                    "custom_instructions": custom_instructions,
                    "include_metadata": include_metadata,
                    "json_options": json_options,
                    "prompt_mode": prompt_mode,
                },
                extract_batch_params.ExtractBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchExtractResponse,
        )

    def stream(
        self,
        *,
        file: FileTypes,
        output_format: str,
        csv_options: str | Omit = omit,
        custom_instructions: str | Omit = omit,
        enable_streaming: bool | Omit = omit,
        file_base64: str | Omit = omit,
        file_url: str | Omit = omit,
        include_metadata: str | Omit = omit,
        json_options: str | Omit = omit,
        prompt_mode: Literal["append", "replace"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ExtractStreamResponse]:
        """
        Stream extraction results via Server-Sent Events (SSE) for real-time content
        delivery.

        **Event Types:**

        - `content`: Incremental content chunks (streaming mode)
        - `complete`: Full content at once (batch mode)
        - `done`: Final event with record_id and processing_time
        - `error`: Error information
        - `async_queued`: Large files queued for async processing

        Provide exactly one of: `file`, `file_url`, or `file_base64`.

        Args:
          file: File to upload (PDF, Word, Excel, PowerPoint, images)

          output_format: Output format(s): `markdown`, `html`, `json`, `csv`. Comma-separate for
              multiple.

          csv_options: CSV extraction options

          custom_instructions: Custom extraction instructions

          enable_streaming: Enable real-time streaming. If false, returns complete content via SSE batch
              mode.

          file_base64: Base64-encoded file content

          file_url: URL to download file from

          include_metadata: Comma-separated metadata: `bounding_boxes`, `confidence_score`

          json_options: JSON extraction options

          prompt_mode: `append`: add to base prompt, `replace`: use only custom instructions

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/extract/stream",
            body=maybe_transform(
                {
                    "file": file,
                    "output_format": output_format,
                    "csv_options": csv_options,
                    "custom_instructions": custom_instructions,
                    "enable_streaming": enable_streaming,
                    "file_base64": file_base64,
                    "file_url": file_url,
                    "include_metadata": include_metadata,
                    "json_options": json_options,
                    "prompt_mode": prompt_mode,
                },
                extract_stream_params.ExtractStreamParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
            stream=True,
            stream_cls=Stream[ExtractStreamResponse],
        )

    def sync(
        self,
        *,
        file: FileTypes,
        output_format: str,
        csv_options: str | Omit = omit,
        custom_instructions: str | Omit = omit,
        file_base64: str | Omit = omit,
        file_url: str | Omit = omit,
        include_metadata: str | Omit = omit,
        json_options: str | Omit = omit,
        prompt_mode: Literal["append", "replace"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractResponse:
        """Process a document and return extracted content immediately.

        (Works for files
        with 5 pages or less.)

        Provide exactly one of: `file`, `file_url`, or `file_base64`.

        Args:
          file: File to upload (PDF, Word, Excel, PowerPoint, images)

          output_format: Output format(s): `markdown`, `html`, `json`, `csv`. Comma-separate for multiple
              (e.g., `markdown,json`).

          csv_options: CSV extraction options (e.g., `table`)

          custom_instructions: Custom extraction instructions (e.g., `Format dates as YYYY-MM-DD`)

          file_base64: Base64-encoded file content

          file_url: URL to download file from

          include_metadata: Comma-separated metadata: `bounding_boxes`, `confidence_score`

          json_options: JSON extraction options. Values: `hierarchy_output`, `table-of-contents`, field
              list `["field1", "field2"]`, or JSON schema `{...}`

          prompt_mode: `append`: add to base prompt, `replace`: use only custom instructions

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/extract/sync",
            body=maybe_transform(
                {
                    "file": file,
                    "output_format": output_format,
                    "csv_options": csv_options,
                    "custom_instructions": custom_instructions,
                    "file_base64": file_base64,
                    "file_url": file_url,
                    "include_metadata": include_metadata,
                    "json_options": json_options,
                    "prompt_mode": prompt_mode,
                },
                extract_sync_params.ExtractSyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )


class AsyncExtractResource(AsyncAPIResource):
    @cached_property
    def results(self) -> AsyncResultsResource:
        return AsyncResultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NanoNets/docstrange-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NanoNets/docstrange-python#with_streaming_response
        """
        return AsyncExtractResourceWithStreamingResponse(self)

    async def async_(
        self,
        *,
        file: FileTypes,
        output_format: str,
        csv_options: str | Omit = omit,
        custom_instructions: str | Omit = omit,
        file_base64: str | Omit = omit,
        file_url: str | Omit = omit,
        include_metadata: str | Omit = omit,
        json_options: str | Omit = omit,
        prompt_mode: Literal["append", "replace"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractResponse:
        """Queue a document for background processing.

        Returns a `record_id` to poll
        results via `GET /api/v1/extract/results/{record_id}`.

        Recommended for large documents (>50 pages).

        Args:
          file: File to upload (PDF, Word, Excel, PowerPoint, images)

          output_format: Output format(s): `markdown`, `html`, `json`, `csv`. Comma-separate for multiple
              (e.g., `markdown,json`).

          csv_options: CSV extraction options (e.g., `table`)

          custom_instructions: Custom extraction instructions (e.g., `Format dates as YYYY-MM-DD`)

          file_base64: Base64-encoded file content

          file_url: URL to download file from

          include_metadata: Comma-separated metadata: `bounding_boxes`, `confidence_score`

          json_options: JSON extraction options. Values: `hierarchy_output`, `table-of-contents`, field
              list `["field1", "field2"]`, or JSON schema `{...}`

          prompt_mode: `append`: add to base prompt, `replace`: use only custom instructions

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/extract/async",
            body=await async_maybe_transform(
                {
                    "file": file,
                    "output_format": output_format,
                    "csv_options": csv_options,
                    "custom_instructions": custom_instructions,
                    "file_base64": file_base64,
                    "file_url": file_url,
                    "include_metadata": include_metadata,
                    "json_options": json_options,
                    "prompt_mode": prompt_mode,
                },
                extract_async_params.ExtractAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    async def batch(
        self,
        *,
        files: SequenceNotStr[FileTypes],
        output_format: str,
        csv_options: str | Omit = omit,
        custom_instructions: str | Omit = omit,
        include_metadata: str | Omit = omit,
        json_options: str | Omit = omit,
        prompt_mode: Literal["append", "replace"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchExtractResponse:
        """Process multiple files asynchronously (max 50 files).

        All files share the same
        extraction options.

        Args:
          files: Files to process (max 50)

          output_format: Output format(s) for all files

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/extract/batch",
            body=await async_maybe_transform(
                {
                    "files": files,
                    "output_format": output_format,
                    "csv_options": csv_options,
                    "custom_instructions": custom_instructions,
                    "include_metadata": include_metadata,
                    "json_options": json_options,
                    "prompt_mode": prompt_mode,
                },
                extract_batch_params.ExtractBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchExtractResponse,
        )

    async def stream(
        self,
        *,
        file: FileTypes,
        output_format: str,
        csv_options: str | Omit = omit,
        custom_instructions: str | Omit = omit,
        enable_streaming: bool | Omit = omit,
        file_base64: str | Omit = omit,
        file_url: str | Omit = omit,
        include_metadata: str | Omit = omit,
        json_options: str | Omit = omit,
        prompt_mode: Literal["append", "replace"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ExtractStreamResponse]:
        """
        Stream extraction results via Server-Sent Events (SSE) for real-time content
        delivery.

        **Event Types:**

        - `content`: Incremental content chunks (streaming mode)
        - `complete`: Full content at once (batch mode)
        - `done`: Final event with record_id and processing_time
        - `error`: Error information
        - `async_queued`: Large files queued for async processing

        Provide exactly one of: `file`, `file_url`, or `file_base64`.

        Args:
          file: File to upload (PDF, Word, Excel, PowerPoint, images)

          output_format: Output format(s): `markdown`, `html`, `json`, `csv`. Comma-separate for
              multiple.

          csv_options: CSV extraction options

          custom_instructions: Custom extraction instructions

          enable_streaming: Enable real-time streaming. If false, returns complete content via SSE batch
              mode.

          file_base64: Base64-encoded file content

          file_url: URL to download file from

          include_metadata: Comma-separated metadata: `bounding_boxes`, `confidence_score`

          json_options: JSON extraction options

          prompt_mode: `append`: add to base prompt, `replace`: use only custom instructions

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/extract/stream",
            body=await async_maybe_transform(
                {
                    "file": file,
                    "output_format": output_format,
                    "csv_options": csv_options,
                    "custom_instructions": custom_instructions,
                    "enable_streaming": enable_streaming,
                    "file_base64": file_base64,
                    "file_url": file_url,
                    "include_metadata": include_metadata,
                    "json_options": json_options,
                    "prompt_mode": prompt_mode,
                },
                extract_stream_params.ExtractStreamParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
            stream=True,
            stream_cls=AsyncStream[ExtractStreamResponse],
        )

    async def sync(
        self,
        *,
        file: FileTypes,
        output_format: str,
        csv_options: str | Omit = omit,
        custom_instructions: str | Omit = omit,
        file_base64: str | Omit = omit,
        file_url: str | Omit = omit,
        include_metadata: str | Omit = omit,
        json_options: str | Omit = omit,
        prompt_mode: Literal["append", "replace"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractResponse:
        """Process a document and return extracted content immediately.

        (Works for files
        with 5 pages or less.)

        Provide exactly one of: `file`, `file_url`, or `file_base64`.

        Args:
          file: File to upload (PDF, Word, Excel, PowerPoint, images)

          output_format: Output format(s): `markdown`, `html`, `json`, `csv`. Comma-separate for multiple
              (e.g., `markdown,json`).

          csv_options: CSV extraction options (e.g., `table`)

          custom_instructions: Custom extraction instructions (e.g., `Format dates as YYYY-MM-DD`)

          file_base64: Base64-encoded file content

          file_url: URL to download file from

          include_metadata: Comma-separated metadata: `bounding_boxes`, `confidence_score`

          json_options: JSON extraction options. Values: `hierarchy_output`, `table-of-contents`, field
              list `["field1", "field2"]`, or JSON schema `{...}`

          prompt_mode: `append`: add to base prompt, `replace`: use only custom instructions

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/extract/sync",
            body=await async_maybe_transform(
                {
                    "file": file,
                    "output_format": output_format,
                    "csv_options": csv_options,
                    "custom_instructions": custom_instructions,
                    "file_base64": file_base64,
                    "file_url": file_url,
                    "include_metadata": include_metadata,
                    "json_options": json_options,
                    "prompt_mode": prompt_mode,
                },
                extract_sync_params.ExtractSyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )


class ExtractResourceWithRawResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.async_ = to_raw_response_wrapper(
            extract.async_,
        )
        self.batch = to_raw_response_wrapper(
            extract.batch,
        )
        self.stream = to_raw_response_wrapper(
            extract.stream,
        )
        self.sync = to_raw_response_wrapper(
            extract.sync,
        )

    @cached_property
    def results(self) -> ResultsResourceWithRawResponse:
        return ResultsResourceWithRawResponse(self._extract.results)


class AsyncExtractResourceWithRawResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.async_ = async_to_raw_response_wrapper(
            extract.async_,
        )
        self.batch = async_to_raw_response_wrapper(
            extract.batch,
        )
        self.stream = async_to_raw_response_wrapper(
            extract.stream,
        )
        self.sync = async_to_raw_response_wrapper(
            extract.sync,
        )

    @cached_property
    def results(self) -> AsyncResultsResourceWithRawResponse:
        return AsyncResultsResourceWithRawResponse(self._extract.results)


class ExtractResourceWithStreamingResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.async_ = to_streamed_response_wrapper(
            extract.async_,
        )
        self.batch = to_streamed_response_wrapper(
            extract.batch,
        )
        self.stream = to_streamed_response_wrapper(
            extract.stream,
        )
        self.sync = to_streamed_response_wrapper(
            extract.sync,
        )

    @cached_property
    def results(self) -> ResultsResourceWithStreamingResponse:
        return ResultsResourceWithStreamingResponse(self._extract.results)


class AsyncExtractResourceWithStreamingResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.async_ = async_to_streamed_response_wrapper(
            extract.async_,
        )
        self.batch = async_to_streamed_response_wrapper(
            extract.batch,
        )
        self.stream = async_to_streamed_response_wrapper(
            extract.stream,
        )
        self.sync = async_to_streamed_response_wrapper(
            extract.sync,
        )

    @cached_property
    def results(self) -> AsyncResultsResourceWithStreamingResponse:
        return AsyncResultsResourceWithStreamingResponse(self._extract.results)
