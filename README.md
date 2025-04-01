# Introduction

This is the multi-lang agnentless for multi-swe-bench.

For python language, please use the original [agentless](https://github.com/OpenAutoCoder/Agentless).

# Setup

```bash
git clone https://github.com/multi-swe-bench/MagentLess.git
cd Magentless

conda create -n magentless python=3.11
conda activate magentless
pip install -r requirements.txt
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

# Data Prepare

Put multi-swe-bench jsonl data in './data', named '{language}_verified.jsonl'.

```bash
cd Magentless
mkdir data
cp java_verified.jsonl data/
...
```

Modify agentless/multilang/utils.py for other data.

# Repo clone

Please clone all the repos into './repo'.

```bash
cd Magentless
mkdir repo
cd repo
git clone https://github.com/dubbo/dubbo.git
...
```

# Patch generation

First create './script/api_key.sh'.

```bash
export OPENAI_API_KEY=
export OPENAI_BASE_URL=
export OPENAI_MODEL=
export OPENAI_EMBED_URL=
```

OPENAI_EMBED_URL is used for embedding retrieval. The default model is 'text-embedding-3-large', which can be modified in agentless/fl/Index.py.

Then modify './script/run.sh'.

```bash
export FOLDER_NAME= # all results in results/FOLDER_NAME
export SWEBENCH_LANG= # {java, javascript, typescript, c, cpp, go, rust}
export PROJECT_FILE_LOC= # See below
export DATASET=local_json # Do not modify
```

You can cache the repo structure in PROJECT_FILE_LOC for speedup, please refer to script/generate_structure.py

Finally run the run.sh

```bash
cd Magentless
bash ./script/run.sh
```

The prediction file and all the logs will be in results/FOLDER_NAME

# Evaluation

Please refer to multi-swe-bench repo.
