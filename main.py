import uvicorn

if __name__ == '__main__':
    config = uvicorn.Config("src.server:app",)
    server = uvicorn.Server(config=config)
    server.run()
