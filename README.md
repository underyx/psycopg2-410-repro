## Usage

```
git clone git@github.com:underyx/psycopg2-410-repro.git
cd psycopg2-410-repro
docker-compose up -d
docker-compose logs -f script | grep unknown -C 10
```

