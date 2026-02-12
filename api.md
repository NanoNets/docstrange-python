# Extract

Types:

```python
from docstrange.types import (
    BatchExtractRequestBody,
    BatchExtractResponse,
    ExtractRequestBody,
    ExtractResponse,
    ExtractionFormatResult,
    ExtractionMetadata,
    ExtractionResult,
    StreamExtractRequestBody,
    ExtractStreamResponse,
)
```

Methods:

- <code title="post /api/v1/extract/async">client.extract.<a href="./src/docstrange/resources/extract/extract.py">async\_</a>(\*\*<a href="src/docstrange/types/extract_async_params.py">params</a>) -> <a href="./src/docstrange/types/extract_response.py">ExtractResponse</a></code>
- <code title="post /api/v1/extract/batch">client.extract.<a href="./src/docstrange/resources/extract/extract.py">batch</a>(\*\*<a href="src/docstrange/types/extract_batch_params.py">params</a>) -> <a href="./src/docstrange/types/batch_extract_response.py">BatchExtractResponse</a></code>
- <code title="post /api/v1/extract/stream">client.extract.<a href="./src/docstrange/resources/extract/extract.py">stream</a>(\*\*<a href="src/docstrange/types/extract_stream_params.py">params</a>) -> str</code>
- <code title="post /api/v1/extract/sync">client.extract.<a href="./src/docstrange/resources/extract/extract.py">sync</a>(\*\*<a href="src/docstrange/types/extract_sync_params.py">params</a>) -> <a href="./src/docstrange/types/extract_response.py">ExtractResponse</a></code>

## Results

Types:

```python
from docstrange.types.extract import ExtractionListResponse, PaginationInfo
```

Methods:

- <code title="get /api/v1/extract/results/{record_id}">client.extract.results.<a href="./src/docstrange/resources/extract/results.py">retrieve</a>(record_id, \*\*<a href="src/docstrange/types/extract/result_retrieve_params.py">params</a>) -> <a href="./src/docstrange/types/extract_response.py">ExtractResponse</a></code>
- <code title="get /api/v1/extract/results">client.extract.results.<a href="./src/docstrange/resources/extract/results.py">list</a>(\*\*<a href="src/docstrange/types/extract/result_list_params.py">params</a>) -> <a href="./src/docstrange/types/extract/extraction_list_response.py">ExtractionListResponse</a></code>

# Classify

Types:

```python
from docstrange.types import (
    BatchClassifyRequestBody,
    BatchClassifyResponse,
    ClassifyRequestBody,
    ClassifyResponse,
    FileClassificationResult,
    PageClassification,
)
```

Methods:

- <code title="post /api/v1/classify/batch">client.classify.<a href="./src/docstrange/resources/classify.py">batch</a>(\*\*<a href="src/docstrange/types/classify_batch_params.py">params</a>) -> <a href="./src/docstrange/types/batch_classify_response.py">BatchClassifyResponse</a></code>
- <code title="post /api/v1/classify/sync">client.classify.<a href="./src/docstrange/resources/classify.py">sync</a>(\*\*<a href="src/docstrange/types/classify_sync_params.py">params</a>) -> <a href="./src/docstrange/types/classify_response.py">ClassifyResponse</a></code>

# Chat

Types:

```python
from docstrange.types import ChatCompletionsRequest
```

Methods:

- <code title="post /v1/chat/completions">client.chat.<a href="./src/docstrange/resources/chat.py">create_completion</a>(\*\*<a href="src/docstrange/types/chat_create_completion_params.py">params</a>) -> object</code>
