# Real-time data pipeline

This projects serves as a baselime for how to create a data pipeline with docker and python, from an API to Grafana, using Kafka, Spark and postgres. 

## Prerequisites 
- Docker Desktop
- DBeaver
- Python (with pip install)

Start up all the services:

```
docker compose up -d
```

Try to run the kafka_generator file and pip install any missing dependencies.

## Postgres
Using a DBeaver, establish a connection with the postgres database. Connection settings:
Host:port = localhost:5432
Find the Postgres user / pw in the Docker environment settings or in the docker compose file. 

Create a table in database "visual" with the following SQL code: 
```
CREATE TABLE stream_loc
(name VARCHAR(100),
latitude FLOAT,
longitude FLOAT)
```
If you can't find the database "visual", check out this solution: https://github.com/dbeaver/dbeaver/issues/1849#issuecomment-661228694

## Grafana
Login to Grafana by going to localhost:3000  
User/pw = admin/admin. You can skip creating new password.  
Navigate to Data Sources (e.g. from left side menu: Configuration --> Data sources, OR Add your first data source on welcome screen)  
Find postgreSQL. The user/pw is in the Docker environment settings, host:port = postgres:5432.
Disable TLS/SSL Mode. Save & Test.
Create a new dashboard (from left side menu: Dashboards --> New dashboard).  
Add a new panel.  
In the query tab (bottom left), choose Format as Table and click on Edit SQL.

```
SELECT name
, latitude
, longitude 
FROM stream_loc
```

On the top right, instead of Time series, choose Geomap. Click Apply.
On the dashboard screen, next to refresh button there is a dropdown menu for refresh frequency. Choose every 5 seconds (5s).

## Pyspark
Navigate to localhost:8888 on your browser to access Jupyter notebooks.
There should be two notebooks. 
First, open 00_Consumer and run all cells. It may take up to 1-2 minutes to get everything started.
The last cell will keep running as it is pulling data from Kafka. 

## Local
In the mean-time, open the kafka_generator notebook from your local machine (e.g. VS Code) and execute it.
(Optional install python packages with: pip install -r requirements.txt)
It will start fetching 2 new users every 4 seconds.

## Pyspark
Navigate back to 00_Consumer notebook in Jupyter. If the last cell has started executing and some folders have appeared (checkpoints, output), then navigate to 04_Postgres. Execute all cells.

## Grafana
Now, go back to Grafana (localhost:3000) and view the dashboard updating every 5 seconds.

Done.
