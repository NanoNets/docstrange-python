# API

## V1

### Extract

Types:

```python
from docstrange.types.api.v1 import (
    ExtractRequestBody,
    ExtractResponse,
    ExtractionFormatResult,
    ExtractBatchResponse,
    ExtractStreamResponse,
)
```

Methods:

- <code title="post /api/v1/extract/async">client.api.v1.extract.<a href="./src/docstrange/resources/api/v1/extract/extract.py">async\_</a>(\*\*<a href="src/docstrange/types/api/v1/extract_async_params.py">params</a>) -> <a href="./src/docstrange/types/api/v1/extract_response.py">ExtractResponse</a></code>
- <code title="post /api/v1/extract/batch">client.api.v1.extract.<a href="./src/docstrange/resources/api/v1/extract/extract.py">batch</a>(\*\*<a href="src/docstrange/types/api/v1/extract_batch_params.py">params</a>) -> <a href="./src/docstrange/types/api/v1/extract_batch_response.py">ExtractBatchResponse</a></code>
- <code title="post /api/v1/extract/stream">client.api.v1.extract.<a href="./src/docstrange/resources/api/v1/extract/extract.py">stream</a>(\*\*<a href="src/docstrange/types/api/v1/extract_stream_params.py">params</a>) -> str</code>
- <code title="post /api/v1/extract/sync">client.api.v1.extract.<a href="./src/docstrange/resources/api/v1/extract/extract.py">sync</a>(\*\*<a href="src/docstrange/types/api/v1/extract_sync_params.py">params</a>) -> <a href="./src/docstrange/types/api/v1/extract_response.py">ExtractResponse</a></code>

#### Results

Types:

```python
from docstrange.types.api.v1.extract import ResultListResponse
```

Methods:

- <code title="get /api/v1/extract/results/{record_id}">client.api.v1.extract.results.<a href="./src/docstrange/resources/api/v1/extract/results.py">retrieve</a>(record_id, \*\*<a href="src/docstrange/types/api/v1/extract/result_retrieve_params.py">params</a>) -> <a href="./src/docstrange/types/api/v1/extract_response.py">ExtractResponse</a></code>
- <code title="get /api/v1/extract/results">client.api.v1.extract.results.<a href="./src/docstrange/resources/api/v1/extract/results.py">list</a>(\*\*<a href="src/docstrange/types/api/v1/extract/result_list_params.py">params</a>) -> <a href="./src/docstrange/types/api/v1/extract/result_list_response.py">ResultListResponse</a></code>

### Classify

Types:

```python
from docstrange.types.api.v1 import (
    FileClassificationResult,
    ClassifyBatchResponse,
    ClassifySyncResponse,
)
```

Methods:

- <code title="post /api/v1/classify/batch">client.api.v1.classify.<a href="./src/docstrange/resources/api/v1/classify.py">batch</a>(\*\*<a href="src/docstrange/types/api/v1/classify_batch_params.py">params</a>) -> <a href="./src/docstrange/types/api/v1/classify_batch_response.py">ClassifyBatchResponse</a></code>
- <code title="post /api/v1/classify/sync">client.api.v1.classify.<a href="./src/docstrange/resources/api/v1/classify.py">sync</a>(\*\*<a href="src/docstrange/types/api/v1/classify_sync_params.py">params</a>) -> <a href="./src/docstrange/types/api/v1/classify_sync_response.py">ClassifySyncResponse</a></code>

# Chat

Methods:

- <code title="post /v1/chat/completions">client.chat.<a href="./src/docstrange/resources/chat.py">create_completion</a>(\*\*<a href="src/docstrange/types/chat_create_completion_params.py">params</a>) -> object</code>
