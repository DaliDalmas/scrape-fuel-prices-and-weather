from os import listdir
from os.path import isfile, join
import pandas as pd
import shutil

def get_runs_to_delete(base_dir: str='./logs', max_runs: int=100)->list:
    runs_to_delete = []
    dags_logs_folders = [dag_log
                            for dag_log in listdir(base_dir)
                            if 'dag_id' in dag_log]

    dags_logs_list = []
    for dag_logs in dags_logs_folders:
        runs = listdir(f'{base_dir}/{dag_logs}')
        number_of_runs = len(runs)
        if number_of_runs > max_runs:
            dags_logs_list+=[[f'{base_dir}/{dag_logs}/{run}',
                                dag_logs,
                                run.split('_')[-1]]
                                for run in runs]

    if len(dags_logs_list)>0:
        dags_logs_df = pd.DataFrame(
            dags_logs_list,
            columns = ['path', 'dag_id', 'run_datetime']
            )

        dags_logs_df['row_num'] = dags_logs_df\
                                    .sort_values(['run_datetime'], ascending=False)\
                                    .groupby('dag_id').cumcount() + 1
        dags_logs_df = dags_logs_df[dags_logs_df['row_num']>max_runs]
        runs_to_delete = list(dags_logs_df['path'].values)

    return runs_to_delete

def delete_directories(paths: list):
    for path in paths:
        shutil.rmtree(path)

def move_directories_to_var_log(paths: list):
    pass

def run():
    paths_to_runs = get_runs_to_delete(base_dir='./logs', max_runs=3)
    delete_directories(paths=paths_to_runs)

if __name__=="__main__":
    run()
