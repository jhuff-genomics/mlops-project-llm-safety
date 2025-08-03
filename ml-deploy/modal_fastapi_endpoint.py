import modal
from pydantic import BaseModel
import time


image = image = modal.Image.debian_slim().uv_sync()
app = modal.App(image=image)


class Item(BaseModel):
    qty: int = 10


def fake_event_streamer(item: Item):
    for i in range(item.qty):
        yield f"data: some data {i}\n\n".encode()
        time.sleep(0.5)


@app.function()
@modal.fastapi_endpoint(method="POST", docs=True)
def stream_me(item: Item):
    from fastapi.responses import StreamingResponse

    return StreamingResponse(fake_event_streamer(item), media_type="text/event-stream")
