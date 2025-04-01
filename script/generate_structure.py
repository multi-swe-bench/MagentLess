import json
import sys

sys.path.append('.')

from tqdm import tqdm

from get_repo_structure.get_repo_structure import get_project_structure_from_scratch

PLAYGROUND = 'playground'
OUT_DIR = 'structure'
LANGUAGE = 'typescript'


def main():
    dataset = []
    with open(f'data/{LANGUAGE}_verified.jsonl', 'r') as fin:
        for line in fin:
            line = line.strip()
            if line:
                dataset.append(json.loads(line))

    for data in tqdm(dataset):
        repo_name = f'{data["org"]}/{data["repo"]}'
        structure = get_project_structure_from_scratch(
            repo_name=repo_name,
            commit_id=data['base']['sha'],
            instance_id=data['instance_id'],
            repo_playground=PLAYGROUND,
        )
        output_file = f'{OUT_DIR}/{data["instance_id"]}.json'
        with open(output_file, 'w') as fout:
            json.dump(structure, fout)


if __name__ == '__main__':
    main()
