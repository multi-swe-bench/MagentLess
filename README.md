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

## 🚀 Magentless: Agentless framework for multi-swe-bench evaluation
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

We are extremely delighted to release **Multi-SWE-Bench**! Multi-SWE-Bench addresses the lack of multilingual benchmarks for evaluating LLMs in real-world code issue resolution. Unlike existing Python-centric benchmarks (e.g., SWE-bench), our framework spans 7 languages (Java, Go, Rust, TypeScript, JavaScript, C, C++) with 1,632 high-quality instances, curated from 2,803 candidates by 88 expert annotators for reliability.
We aim to accelerate progress in automated issue resolution and RL, bridging the gap toward AGI. Let's join the **Multi-SWE-RL community** to expand datasets, tools, and research collaboration!

This repo provides Magentless, the [Agentless](https://github.com/OpenAutoCoder/Agentless) framework compatible with [multi-swe-bench](https://github.com/multi-swe-bench/multi-swe-bench).

## ⚡ Features
- **Comprehensive Evaluation**: Tests top models (GPT-4o, Claude 3.5/3.7, DeepSeek V3/R1, Doubao-Pro, etc.) across frameworks (Agentless, SWE-agent, OpenHands), yielding actionable insights.  
- **Multi-SWE-RL Community**: Open-source initiative for large-scale reinforcement learning (RL) datasets. Initial release includes **4723 structured instances** across languages to advance RL research.  
- **Open Infrastructure**: Full data pipeline and tutorials open-sourced to foster community contributions and scalability.  

## 📢 News
[2025/03/XX]🔥We have supported XXXXXX.
<br>
[2025/02/XX]🔥XXX is accepted as XXXXXX.
<br>
[2025/01/XX]🔥We release XXX.

## 📊 Evaluation

### Introduction

This is the magnentless for multi-swe-bench.

For python language, please use the original [agentless](https://github.com/OpenAutoCoder/Agentless).

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

### Evaluation

Please refer to [multi-swe-bench](https://github.com/multi-swe-bench/multi-swe-bench) repo.


## [🏆 Multi-SWE-RL Community](https://huggingface.co/Multi-SWE-RL)
[📋 Multi-SWE-RL Dataset Overview](https://docs.google.com/spreadsheets/d/1C90SiRmlac3FizmsJzxzrhSNsnCjyYewdrXzFbBV4x0/edit?gid=493937140#gid=493937140)

The Multi-SWE-RL Community is an open-source initiative focused on collaborative dataset creation for software engineering and reinforcement learning research. To foster active participation and recognize contributors, we introduce this Contribution Incentive Plan. By contributing high-quality data, you directly support advancements in AI research and earn recognition within the community. 

**Incentive Tiers:**
1. **Be a Contributor**: Get listed in the [Contribution Progress Sheet](https://docs.google.com/spreadsheets/d/1C90SiRmlac3FizmsJzxzrhSNsnCjyYewdrXzFbBV4x0/
2. **Report Authorship**: Become an author in future technical reports

Full details: [Contribution Incentive Plan](docs/contribution-incentive-plan.md)

**Get Started in 2 Steps:**
1. **Learn**: [Quick-Start Guide](docs/build-dataset-quick-start.md)
2. **Try**: Follow our [Contribution Demo](docs/contribution-demo.md 

## 🌟 Star Growth Trends

<p align="center">
  <a href="https://star-history.com/#multi-swe-bench/multi-swe-bench&Date">
    <img src="https://api.star-history.com/svg?repos=multi-swe-bench/multi-swe-bench&type=Date" width="500" alt="Star History Chart">
  </a>
</p>

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

