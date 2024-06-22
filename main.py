import uvicorn

if __name__ == '__main__':
    config = uvicorn.Config("src.server:app", host='0.0.0.0')
    server = uvicorn.Server(config=config)
    server.run()
