# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ChatCreateCompletionParams", "Message", "MessageContent", "MessageContentFileURL", "MessageContentImageURL"]


class ChatCreateCompletionParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    model: Required[str]

    stream: bool


class MessageContentFileURL(TypedDict, total=False):
    url: str


class MessageContentImageURL(TypedDict, total=False):
    url: str


class MessageContent(TypedDict, total=False):
    file_url: MessageContentFileURL

    image_url: MessageContentImageURL

    text: str

    type: str


class Message(TypedDict, total=False):
    content: Required[Iterable[MessageContent]]

    role: Required[str]
