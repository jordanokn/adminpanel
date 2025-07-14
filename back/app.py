from contextlib import asynccontextmanager

from litestar import Litestar
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin

from container import container


@asynccontextmanager
async def lifespan(_):
    db = container.db()
    await db.connect()
    yield
    await db.close()


app = Litestar(
    lifespan=[lifespan],
    openapi_config=OpenAPIConfig(
        title="API", version="1.0.0", render_plugins=[SwaggerRenderPlugin()]
    ),
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, host="127.0.0.1", port=8000)
