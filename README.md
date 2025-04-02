<div align="center">
 👋 Hi, everyone! 
    <br>
    We are <b>ByteDance Seed team.</b>
</div>

<p align="center">
  You can get to know us better through the following channels👇
  <br>
  <a href="https://team.doubao.com/">
    <img src="https://img.shields.io/badge/Website-%231e37ff?style=for-the-badge&logo=bytedance&logoColor=white"></a>
  <a href="https://github.com/user-attachments/assets/93481cda-a7f3-47f3-b333-fe6b3da86b78">
    <img src="https://img.shields.io/badge/WeChat-07C160?style=for-the-badge&logo=wechat&logoColor=white"></a>
 <a href="https://www.xiaohongshu.com/user/profile/668e7e15000000000303157d?xsec_token=ABl2-aqekpytY6A8TuxjrwnZskU-6BsMRE_ufQQaSAvjc%3D&xsec_source=pc_search">
    <img src="https://img.shields.io/badge/Xiaohongshu-%23FF2442?style=for-the-badge&logo=xiaohongshu&logoColor=white"></a>
  <a href="https://www.zhihu.com/org/dou-bao-da-mo-xing-tuan-dui/">
    <img src="https://img.shields.io/badge/zhihu-%230084FF?style=for-the-badge&logo=zhihu&logoColor=white"></a>
</p>

![seed logo](https://github.com/user-attachments/assets/c42e675e-497c-4508-8bb9-093ad4d1f216)

## 🚀 Magentless: Agentless for multi-swe-bench
<p align="center">
  <a href="https://github.com/multi-swe-bench/multi-swe-bench">
    <img src="https://img.shields.io/badge/Multi_SWE_bench-Project Page-yellow"></a>
  <a href="https://arxiv.org/pdf/2502.19811">
    <img src="https://img.shields.io/badge/Multi_SWE_bench-Tech Report-red"></a>
  <a href="https://huggingface.co/datasets/Multi-SWE-RL/Multi-SWE-Bench">
    <img src="https://img.shields.io/badge/Multi_SWE_bench-Hugging Face-orange"></a>
  <br>
  <a href="https://huggingface.co/Multi-SWE-RL">
    <img src="https://img.shields.io/badge/Multi_SWE_RL_Community-Hugging Face-EE9A12"></a>
  <a href="https://discord.gg/EtfbkfqUuN">
    <img src="https://img.shields.io/badge/Multi_SWE_RL_Community-Discord-1449DA"></a>
  <a href="https://github.com/multi-swe-bench/multi-swe-bench/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-Apache-blue"></a>
</p>

This repo provides Magentless, which is based on [agentless](https://github.com/OpenAutoCoder/Agentless) framework and compatible with [multi-swe-bench](https://github.com/multi-swe-bench/multi-swe-bench). Magentless supports C++, C, Java, Go, Rust, Typescript and Javascript. For python language, please use the original agentless.

## 📊 Evaluation

### Setup

```bash
git clone https://github.com/multi-swe-bench/MagentLess.git
cd Magentless

conda create -n magentless python=3.11
conda activate magentless
pip install -r requirements.txt
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

### Data Preparation

Put multi-swe-bench jsonl data in './data', named '{language}_verified.jsonl'.

```bash
cd Magentless
mkdir data
cp java_verified.jsonl data/
...
```

Modify agentless/multilang/utils.py for other data.

### Repo cloning

Please clone all the repos into './repo'.

```bash
cd Magentless
mkdir repo
cd repo
git clone https://github.com/dubbo/dubbo.git
...
```

### Patch generation

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
export FOLDER_NAME= # all results are in results/FOLDER_NAME
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

### Evaluation

Please refer to [multi-swe-bench](https://github.com/multi-swe-bench/multi-swe-bench) repo.

## 📜 License
This project is licensed under Apache License 2.0. See the [LICENSE](/LICENSE) flie for details.

## 📖 Citation
If you find XXX useful for your research and applications, feel free to give us a star ⭐ or cite us using:

```bibtex
@article{zan2024swe,
  title={Swe-bench-java: A github issue resolving benchmark for java},
  author={Zan, Daoguang and Huang, Zhirong and Yu, Ailun and Lin, Shaoxin and Shi, Yifan and Liu, Wei and Chen, Dong and Qi, Zongshuai and Yu, Hao and Yu, Lei and others},
  journal={arXiv preprint arXiv:2408.14354},
  year={2024}
}
```

## 🏢 About [ByteDance Seed Team](https://team.doubao.com/)
Founded in 2023, ByteDance Seed Team is dedicated to crafting the industry's most advanced AI foundation models. The team aspires to become a world-class research team and make significant contributions to the advancement of science and society.

