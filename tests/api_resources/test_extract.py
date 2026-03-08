# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from docstrange import Docstrange, AsyncDocstrange
from tests.utils import assert_matches_type
from docstrange.types import (
    ExtractResponse,
    BatchExtractResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtract:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_async(self, client: Docstrange) -> None:
        extract = client.extract.async_(
            output_format="markdown",
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_async_with_all_params(self, client: Docstrange) -> None:
        extract = client.extract.async_(
            output_format="markdown",
            csv_options="",
            custom_instructions="",
            file=b"Example data",
            file_base64="",
            file_url="",
            include_metadata="",
            json_options="",
            prompt_mode="append",
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_async(self, client: Docstrange) -> None:
        response = client.extract.with_raw_response.async_(
            output_format="markdown",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_async(self, client: Docstrange) -> None:
        with client.extract.with_streaming_response.async_(
            output_format="markdown",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch(self, client: Docstrange) -> None:
        extract = client.extract.batch(
            files=[b"Example data"],
            output_format="markdown",
        )
        assert_matches_type(BatchExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_with_all_params(self, client: Docstrange) -> None:
        extract = client.extract.batch(
            files=[b"Example data"],
            output_format="markdown",
            csv_options="csv_options",
            custom_instructions="custom_instructions",
            include_metadata="include_metadata",
            json_options="json_options",
            prompt_mode="append",
        )
        assert_matches_type(BatchExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_batch(self, client: Docstrange) -> None:
        response = client.extract.with_raw_response.batch(
            files=[b"Example data"],
            output_format="markdown",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(BatchExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_batch(self, client: Docstrange) -> None:
        with client.extract.with_streaming_response.batch(
            files=[b"Example data"],
            output_format="markdown",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(BatchExtractResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream(self, client: Docstrange) -> None:
        extract_stream = client.extract.stream(
            output_format="markdown",
        )
        extract_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_with_all_params(self, client: Docstrange) -> None:
        extract_stream = client.extract.stream(
            output_format="markdown",
            csv_options="",
            custom_instructions="",
            enable_streaming=True,
            file=b"Example data",
            file_base64="",
            file_url="",
            include_metadata="",
            json_options="",
            prompt_mode="append",
        )
        extract_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream(self, client: Docstrange) -> None:
        response = client.extract.with_raw_response.stream(
            output_format="markdown",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream(self, client: Docstrange) -> None:
        with client.extract.with_streaming_response.stream(
            output_format="markdown",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sync(self, client: Docstrange) -> None:
        extract = client.extract.sync(
            output_format="markdown",
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sync_with_all_params(self, client: Docstrange) -> None:
        extract = client.extract.sync(
            output_format="markdown",
            csv_options="",
            custom_instructions="",
            file=b"Example data",
            file_base64="",
            file_url="",
            include_metadata="",
            json_options="",
            prompt_mode="append",
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_sync(self, client: Docstrange) -> None:
        response = client.extract.with_raw_response.sync(
            output_format="markdown",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_sync(self, client: Docstrange) -> None:
        with client.extract.with_streaming_response.sync(
            output_format="markdown",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExtract:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_async(self, async_client: AsyncDocstrange) -> None:
        extract = await async_client.extract.async_(
            output_format="markdown",
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_async_with_all_params(self, async_client: AsyncDocstrange) -> None:
        extract = await async_client.extract.async_(
            output_format="markdown",
            csv_options="",
            custom_instructions="",
            file=b"Example data",
            file_base64="",
            file_url="",
            include_metadata="",
            json_options="",
            prompt_mode="append",
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_async(self, async_client: AsyncDocstrange) -> None:
        response = await async_client.extract.with_raw_response.async_(
            output_format="markdown",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_async(self, async_client: AsyncDocstrange) -> None:
        async with async_client.extract.with_streaming_response.async_(
            output_format="markdown",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch(self, async_client: AsyncDocstrange) -> None:
        extract = await async_client.extract.batch(
            files=[b"Example data"],
            output_format="markdown",
        )
        assert_matches_type(BatchExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_with_all_params(self, async_client: AsyncDocstrange) -> None:
        extract = await async_client.extract.batch(
            files=[b"Example data"],
            output_format="markdown",
            csv_options="csv_options",
            custom_instructions="custom_instructions",
            include_metadata="include_metadata",
            json_options="json_options",
            prompt_mode="append",
        )
        assert_matches_type(BatchExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncDocstrange) -> None:
        response = await async_client.extract.with_raw_response.batch(
            files=[b"Example data"],
            output_format="markdown",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(BatchExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncDocstrange) -> None:
        async with async_client.extract.with_streaming_response.batch(
            files=[b"Example data"],
            output_format="markdown",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(BatchExtractResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream(self, async_client: AsyncDocstrange) -> None:
        extract_stream = await async_client.extract.stream(
            output_format="markdown",
        )
        await extract_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncDocstrange) -> None:
        extract_stream = await async_client.extract.stream(
            output_format="markdown",
            csv_options="",
            custom_instructions="",
            enable_streaming=True,
            file=b"Example data",
            file_base64="",
            file_url="",
            include_metadata="",
            json_options="",
            prompt_mode="append",
        )
        await extract_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncDocstrange) -> None:
        response = await async_client.extract.with_raw_response.stream(
            output_format="markdown",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncDocstrange) -> None:
        async with async_client.extract.with_streaming_response.stream(
            output_format="markdown",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sync(self, async_client: AsyncDocstrange) -> None:
        extract = await async_client.extract.sync(
            output_format="markdown",
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sync_with_all_params(self, async_client: AsyncDocstrange) -> None:
        extract = await async_client.extract.sync(
            output_format="markdown",
            csv_options="",
            custom_instructions="",
            file=b"Example data",
            file_base64="",
            file_url="",
            include_metadata="",
            json_options="",
            prompt_mode="append",
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_sync(self, async_client: AsyncDocstrange) -> None:
        response = await async_client.extract.with_raw_response.sync(
            output_format="markdown",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_sync(self, async_client: AsyncDocstrange) -> None:
        async with async_client.extract.with_streaming_response.sync(
            output_format="markdown",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True
