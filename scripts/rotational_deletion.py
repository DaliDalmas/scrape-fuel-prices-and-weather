from os import listdir
from os.path import isfile, join
import pandas as pd
import shutil

class RotationalDeletion:
    def __init__(self) -> None:
        self.base_dir: str = './airflow/logs'
        self.max_runs: int = 3
        self.max_scheduler_days: int = 3

    def get_runs_to_delete(self)->list:
        runs_to_delete = []
        dags_logs_folders = [dag_log
                                for dag_log in listdir(self.base_dir)
                                if 'dag_id' in dag_log]

        dags_logs_list = []
        for dag_logs in dags_logs_folders:
            runs = listdir(f'{self.base_dir}/{dag_logs}') 
            number_of_runs = len(runs)
            if number_of_runs > self.max_runs:
                dags_logs_list+=[[f'{self.base_dir}/{dag_logs}/{run}',
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
            dags_logs_df = dags_logs_df[dags_logs_df['row_num']>self.max_runs]
            runs_to_delete = list(dags_logs_df['path'].values)
            print(f"Deletiing {len(runs_to_delete)} log runs from dag runs")
        
        # getting scheduler days logs to delete
        scheduler_logs_folders = [scheduler_log for scheduler_log in listdir(self.base_dir+'/scheduler' ) if 'latest' not in scheduler_log]
        scheduler_logs_list = []
        for folder in scheduler_logs_folders:
            scheduler_logs_list.append([folder, f'{self.base_dir}/scheduler/{folder}'])
        if len(scheduler_logs_list)>0:
            scheduler_logs_df = pd.DataFrame(
                scheduler_logs_list,
                columns = ['date', 'path']
                )
            scheduler_logs_df = scheduler_logs_df.sort_values(by = ['date'], ascending=False)
            scheduler_days_to_delete = list(scheduler_logs_df['path'].tail(scheduler_logs_df.shape[0]-self.max_scheduler_days))
            print(f"Deletiing {len(scheduler_days_to_delete)} log day(s) from scheduler")

        folders_to_delete = scheduler_days_to_delete+runs_to_delete

        return folders_to_delete

    def delete_directories(self, paths: list):
        for path in paths:
            shutil.rmtree(path)

    def run(self):
        paths_to_folders = self.get_runs_to_delete()
        print(paths_to_folders)
        #self.delete_directories(paths=paths_to_folders)

if __name__=="__main__":
    RotationalDeletion().run()
