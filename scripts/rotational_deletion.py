from os import listdir
import pandas as pd
import shutil


class RotationalDeletion:
    """
    Deletes airflow logs from the base_log_folder spacified here
    as base_dir.
        params: None
        returns: None
    """
    def __init__(self) -> None:
        """
        base_dir: The base_log_folder
        max_runs: The maximum number of run logs that should remain undeleted
        max_scheduler_days: The number of days of logs that should remain undeleted
            for scheduler logs
        """
        self.base_dir: str = '/var/log/airflow'
        self.max_runs: int = 100
        self.max_scheduler_days: int = 100

    def get_runs_to_delete(self) -> list:
        """
        gets all folders in the base_dir that are to be deleted
        params: None
        returns: list of paths to the folders to be deleted
        """

        # getting runs logs to be deleted
        runs_to_delete = []
        dags_logs_folders = [dag_log
                             for dag_log in listdir(self.base_dir)
                             if 'dag_id' in dag_log]

        dags_logs_list = []
        for dag_logs in dags_logs_folders:
            runs = listdir(f'{self.base_dir}/{dag_logs}')
            number_of_runs = len(runs)
            if number_of_runs > self.max_runs:
                dags_logs_list += [[f'{self.base_dir}/{dag_logs}/{run}',
                                    dag_logs,
                                    run.split('_')[-1]]
                                   for run in runs]

        if len(dags_logs_list) > 0:
            dags_logs_df = pd.DataFrame(
                dags_logs_list,
                columns=['path', 'dag_id', 'run_datetime']
                )

            dags_logs_df['row_num'] = dags_logs_df\
                .sort_values(['run_datetime'], ascending=False)\
                .groupby('dag_id').cumcount() + 1
            dags_logs_df = dags_logs_df[dags_logs_df['row_num'] > self.max_runs]
            runs_to_delete = list(dags_logs_df['path'].values)
            print(f"Deletiing {len(runs_to_delete)} log runs from dag runs")
        else:
            runs_to_delete = []

        # getting scheduler days logs to delete
        scheduler_logs_folders = [scheduler_log for scheduler_log in
                                  listdir(self.base_dir+'/scheduler') if 'latest' not in scheduler_log]
        scheduler_logs_list = []
        for folder in scheduler_logs_folders:
            scheduler_logs_list.append([folder, f'{self.base_dir}/scheduler/{folder}'])
        if len(scheduler_logs_list) > 0:
            scheduler_logs_df = pd.DataFrame(
                scheduler_logs_list,
                columns=['date', 'path']
                )
            scheduler_logs_df = scheduler_logs_df.sort_values(by=['date'], ascending=False)
            df_len = scheduler_logs_df.shape[0]
            if df_len > self.max_scheduler_days:
                scheduler_days_to_delete = list(scheduler_logs_df['path']
                                                .tail(scheduler_logs_df.shape[0]-self.max_scheduler_days))
            else:
                scheduler_days_to_delete = []
            print(f"Deletiing {len(scheduler_days_to_delete)} log day(s) from scheduler")
        else:
            scheduler_days_to_delete = []

        folders_to_delete = scheduler_days_to_delete+runs_to_delete

        return folders_to_delete

    def delete_directories(self, paths: list) -> None:
        """
        deletes folders
        params paths: list of paths of folders to be deleted
        returns: None
        """
        for path in paths:
            shutil.rmtree(path)

    def run(self) -> None:
        """
        Executes the whole process of finding the folders to be deleted then
        deleting them
        """
        paths_to_folders = self.get_runs_to_delete()
        print(paths_to_folders)
        self.delete_directories(paths=paths_to_folders)


if __name__ == "__main__":
    RotationalDeletion().run()
