import json
from .llm import stream_output

def sse_generator(messages):
    stream = stream_output(messages)

    for chunk in stream:
        if not chunk.choices:
            continue
        delta = chunk.choices[0].delta
        content = getattr(delta, "content", None)
        if content:
            data = {
                "choices": [{
                    "delta": {"content": content},
                    "index": 0
                }]
            }
            yield f"data: {json.dumps(data, ensure_ascii=False)}\n\n"

    yield "data: [DONE]\n\n"