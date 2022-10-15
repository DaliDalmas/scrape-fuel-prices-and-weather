create user airflow_user2 with password 'airflow';
create user fastapi_user2 with password 'fastapi';
GRANT USAGE ON SCHEMA airflow, scraped_data, public TO airflow_user2 ;
GRANT USAGE ON SCHEMA airflow, scraped_data, public TO fastapi_user2 ;
GRANT create ON SCHEMA airflow, scraped_data, public TO airflow_user2 ;
GRANT create ON SCHEMA airflow, scraped_data, public TO fastapi_user2 ;


GRANT SELECT ON ALL TABLES IN SCHEMA airflow, scraped_data, public TO airflow_user2 ;
GRANT insert ON ALL TABLES IN SCHEMA airflow, scraped_data, public TO airflow_user2 ;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA airflow, scraped_data, public TO airflow_user2 ;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA airflow, scraped_data, public TO airflow_user2 ;

GRANT ALL ON ALL TABLES IN SCHEMA airflow, scraped_data, public TO fastapi_user2 ;
GRANT ALL ON ALL SEQUENCES IN SCHEMA airflow, scraped_data, public TO fastapi_user2 ;
GRANT ALL ON ALL FUNCTIONS IN SCHEMA airflow, scraped_data, public TO fastapi_user2 ;