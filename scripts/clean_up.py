from os import listdir, remove

def clean_up():
    base_dir = './tmp'
    paths = [dag_log for dag_log in listdir(base_dir)]
    for path in paths:
        remove(f'{base_dir}/{path}')