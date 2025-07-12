from starlite import Starlite

app = Starlite(route_handlers=[])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app)
