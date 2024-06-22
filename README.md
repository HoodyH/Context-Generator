# Contex generator

Ai companion to edit word files

Software requred to run the code or to develop
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Python](https://www.python.org/)
- [Drawio](https://www.drawio.com/)

## Configure development environment

Install dependencies
```bash
python -m pip install -r requirements.txt
```

Run the app
```bash
python main.py
```
open the app at [localhost](http://127.0.0.1:8000)

## Run as a production docker container

- create a file `.env` in the folder root with open apy key, like the following example
```text
OPENAI_API_KEY=sk-proj-JHASJHw2iFhaksdkhasdfllbkFJfwhlasjdflkasdjflr
```
- open a terminar in the root of the folder and start the container with the following command
```bash
docker-compose up -d
```

Now you can open the app at [localhost](http://127.0.0.1:8000) or use it in the ip host of the machine

To find the ip host use
```bash
ipconfig
```
