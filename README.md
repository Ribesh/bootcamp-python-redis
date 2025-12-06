# README

### Step 1:
>Edit the `requirements.txt` file to add `psycopg2-binary` library

### Step 2:
>Edit the `app.py` to include `check_postgres()` function at path `/db`

### Step3: 
>Updated the `docker-compose.yaml` file to include `postgres` container

### Step 4:
In the directory containing the `docker-compose.yaml` run the below command 👇
```bash
docker compose up -d
```

### Step 5:
Verify
```bash
docker ps
```

![alt text](Images/image.png)


### Step 6:
Use `curl` command to verify the endpoints

```bash
#for redis
curl http://localhost

#for postgres
curl http://localhost/db
```

![alt text](Images/image-1.png)

### Step 7:
>Sanity Checks

#### A. Stopping both containers
```bash
docker stop redis postgres
```

![alt text](Images/image-2.png)

#### B. Stopping either of the containers
```bash
docker stop redis
```

![alt text](Images/image-3.png)