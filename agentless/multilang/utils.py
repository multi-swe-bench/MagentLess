import json
from pathlib import Path

from agentless.multilang.const import LANGUAGE, LANG_EXT


def process(raw_data):
    raw = json.loads(raw_data)
    data = {
        'repo': f'{raw["org"]}/{raw["repo"]}',
        'instance_id': raw['instance_id'],
        'base_commit': raw['base']['sha'],
        'problem_statement': raw['resolved_issues'][0]['title'] + '\n' + raw['resolved_issues'][0]['body'],
    }
    return data


def load_local_json():
    dataset = []
    if LANGUAGE == 'javascript':
        lang = 'js'
    elif LANGUAGE == 'typescript':
        lang = 'ts'
    else:
        lang = LANGUAGE
    path = Path(f'data/{lang}')
    lines = []
    for file in path.iterdir():
        lines.extend(file.read_text().splitlines())
    dataset = [process(x) for x in lines]
    return dataset


def end_with_ext(file_name):
    for ext in LANG_EXT:
        if file_name.endswith(f'.{ext}'):
            return True
    return False
