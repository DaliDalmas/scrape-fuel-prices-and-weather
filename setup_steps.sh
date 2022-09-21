 1004  pyenv local 3.9.9
 1005  git clone https://github.com/DaliDalmas/scrape-epl-news.git
 1006  cd scrape-epl-news
 1007  pyenv local 3.9.9
 1008  pip install --upgrade pip
 1009  python -m venv venv
 1010  source venv/bin/activate
 1011  pip install pandas jupyterlab beautifulsoup4 psycopg2-binary seaborn plotly "apache-airflow[s3]" 