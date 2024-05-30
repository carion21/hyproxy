# hyproxy
A little code to create a proxy that can be easily deployed on any hosting. Its role is to hide and serve as a gateway between an API, for example deployed on a server with a public url: http.s://ip:port

```bash
pipenv shell

pipenv install

python main.py

```

```bash
curl -X GET http://localhost:9191/api/v1/health

```

### By Carion21 ;)