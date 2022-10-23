# scrape weather and fuel prices
In this project I used apache airflow to scrape website periodically. This is for the tutorials I do on youtube. You can checkout my channel [here](https://www.youtube.com/channel/UCzSlSeJ4XH4bWH79DKmIxjg). I do data science and data engineering videos for projects like these.
## Technologies used
<img src="images/beautifulsoup.png" alt="Apache Airflow" width="200" height="100"/>&nbsp;&nbsp;<img src="images/AirflowLogo.png" alt="BeautifulSoup" width="200" height="100" />&nbsp;&nbsp;<img src="images/fastapi.png" alt="fast api" width="200" height="100" />

<img src="images/postgresql.png" alt="postgresql" width="200"  height="100" />&nbsp;&nbsp;<img src="images/dash.png" alt="dash" width="200" height="100" />&nbsp;&nbsp;<img src="images/alchemy.jpeg" alt="sqlalchemy" width="200" height="100" />

## using the project
You can follow these steps to setup and you can use [this video]() to help you understand what is going on.
1. Clone this repo.
2. cd into the repo 
```
cd scrape-epl-news
```
3. Run `setup_steps` to install dependencies. Make sure you are using `pyenv` to manage your python versions and `python 3.10.0` is installed in the pyenv manager.
```
bash scripts/setup_steps.sh
```

## setting up airflow

1. activate the virtual environment
```
source venv activate
```

2. set the `PYTHONPATH` environment variable
```
export PYTHONPATH
```

3. set the `AIRFLOW_HOME` variable
```
export AIRFLOW_HOME
```

4. initiate airflow by running `airflow version` command. This command is used to check the verion of airflow but it also helps to create the airflow config file in `AIRFLOW_HOME`
```
airflow version
```

5. Open `airflow.cfg` file created inside `AIRFLOW_HOME` and change the following parameters
```
sql_alchemy_conn = postgresql+psycopg2://<<username>>:<<password>>@<<host>>/<database>
```
This is because this project used postgres database to manage all metadata for airflow

6. Initialise the database
```
airflow db init
```

7. create airflow users
```
airflow users create --username name --firstname Fname --lastname Lname --role Admin --email name@name.com --password pass
```

## running fastapi
fast api is used to manage the database iteractions. If the api is down no data will be submitted to the database. To run fastapi
1. cd into the repo
2. activate the virtual environment
```
source venv/bin/activate
```
3. run the following command
```
uvicorn api.main:app
```
4. You can access the api documentation on `http://127.0.0.1:8000/docs`

## running airflow
1. Open fresh terminal
2. cd into the repo
3. set the following environment variables as follows
```
export PYTHONPATH=`pwd`
export AIRFLOW_HOME=`pwd`/airflow
```
4. activate the virtual environment
```
source venv/bin/activate
```
5. run airflow scheduler
```
airflow scheduler
```
6. Open another fresh terminal and follow steps `2` to `4`
7. run airflow webserver
```
airflow webserver
```
8. you can access airflow ui on `http://0.0.0.0:8080/`

Note: ensure both terminals remain open for airflow to continue working

## running dash 
1. Open fresh terminal
2. cd into the repo
3. activate the virtual environment
```
source venv/bin/activate
```
4. run the following command to have dash running
```
python dash/app.py
```
5. you can access dash on `http://127.0.0.1:8050/`