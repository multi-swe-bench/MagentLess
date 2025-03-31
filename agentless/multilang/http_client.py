import json
import os

import requests

URL = os.environ.get('SWEBENCH_URL', '')
HEADERS = {
    'Content-Type': 'application/json'
}
TIMEOUT = 300


def run_instance_in_remote(func, sample, pred, run_id):
    instance_id = sample['instance_id']
    record = dict(**pred)
    record.update({'dataset': sample})
    record['dataset']['created_at'] = str(record['dataset']['created_at'])

    res = func(record=record)
    print(res)
    if 'detail' in res:
        detail_dir = f'logs/run_evaluation/{run_id}/test/{instance_id}'
        os.makedirs(detail_dir, exist_ok=True)

        report_json_path = f'{detail_dir}/report.json'
        with open(report_json_path, 'w') as f:
            f.write(res['detail']['report_json'])
        print(f'Write {report_json_path} success.')

        test_output_txt_path = f'{detail_dir}/test_output.txt'
        with open(test_output_txt_path, 'w') as f:
            f.write(res['detail']['test_output_txt'])
        print(f'Write {test_output_txt_path} success.')

    return instance_id, res


def bench_run_regression_test(record):
    eval_spec = {
        'result_detail_return': True,
    }
    payload = json.dumps({
        'eval_spec': eval_spec,
        'record': record,
    })

    resp = requests.request('POST', f'{URL}/bench/run_regression_test', headers=HEADERS, data=payload, timeout=TIMEOUT)
    resp.raise_for_status()

    content = json.loads(resp.content)
    if content['code'] != 0:
        return content

    context = content['data']
    return context.get('report')

