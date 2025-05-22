import json
import os

import requests

URL = os.environ.get('SWEBENCH_URL', '')
HEADERS = {
    'Content-Type': 'application/json'
}
TIMEOUT = 300


def run_instance_in_remote(func, sample, pred, run_id):
    '''
        NOT USED
    '''
    pass

def bench_run_regression_test(record):
    '''
        NOT USED
    '''
    pass

