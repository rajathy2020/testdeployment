# hy-esm
ESM V2

## Start Backend with remote DB connected

### Prepare env file
;Since we are using remote db via SSH tunnel, we need to define DB_SERVER ssh connection with user@host

DB_SERVER=ubuntu@developmentdeploy.hytechnologies.co

;SSH tunnel will be binded to localhost in docker container

TK_COUCH_HOST_URL=http://localhost:5984

;Enter couchdb password of remote server

TK_COUCH_PASS=couchpass

### Prepare SSH private key volume mount

- Since we are connecting remote couchdb via SSH tunnel we need to provide our SSH key which is authenticated to connect to server

- Make sure the path is binded properly in docker-compose-local.yml

- ```- /home/ubuntu/.ssh/id_rsa.pem:/root/id_rsa.pem```

### Start backend

```sudo docker-compose -f docker-compose-local.yml up api``` (API only)

```sudo docker-compose -f docker-compose-local.yml up api jupyter``` (API and Jupyter)

### Implementation detail

We have custom entrypoint shell file (backend/run_api_with_remote_db.sh) which first connects to remote couchdb via SSH tunnel and then starts Uvicorn

### Enable SSL

We can also enable SSL on local API via Uvicorn

- Uncomment ```uvicorn --fd 0 code.api.api:app --host="0.0.0.0" --ssl-keyfile="/ssl/localhost.key" --ssl-certfile="/ssl/localhost.crt" --port=8090 --reload``` in backend/run_api_with_remote_db.sh and comment other uvicorn command

- Make sure you have self signed ssl certificates in ssl directory of codebase (volume mounted ```- ./ssl:/ssl``` in docker-compose-local.yml)


## Start Backend

```docker-compose -f docker-compose.yml -f docker-compose.local.yml up api``` (API only)

## Start frontend

```npm run serve```

https://localhost:8080/


## Build frontend

```npm run build```