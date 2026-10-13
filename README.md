# local-ai-replicator

### **A 100% local, nontechnical friendly step-by-step pipeline combining `ComfyUI` and `ai-toolkit` to train and generate ultra-realistic custom LoRAs of real-world subjects.**

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Workflow-orange.svg)](https://github.com/comfyanonymous/ComfyUI)
[![ai-toolkit](https://img.shields.io/badge/ai--toolkit-ostris-purple.svg)](https://github.com/ostris/ai-toolkit)

Whether you are building a digital double of a person or capturing unique real-world objects, this repository guides you through every step creating your own high-fidelity LoRAs on your consumer hardware with full privacy, for free.

## What is a LoRA?

A **LoRA** (`Low-Rank Adaptation`) is a small, lightweight "patch file" for a larger AI model. Instead of spending weeks retraining a massive multi-gigabyte base model from scratch, we take a free, photorealistic base model (like `CyberRealismXL`) and fine-tune a small layer of weights using a curated set of photos. As a result, you get a compact (~100 MB - 300 MB) custom file that teaches the base model how to recreate your specific subject with near-1:1 visual precision.

---

## Key Features & Advantages

- **100% Local & Private:** Runs entirely on your hardware. Your images and generations never leave your PC.
- **Photorealistic Accuracy:** Pre-configured hyperparameters designed to achieve near-1:1 subject replication.
- **Zero Restrictions:** Native support for unrestricted base models, bypassing cloud service content filters.
- **Workflow Presets:** Includes `ComfyUI` and `ai-toolkit` templates for instant easy drag-and-drop use.

## Instruction Overview & Guide

Follow the guide sequentially by navigating into each step's folder:

| Step | Section | Description |
| :---: | :--- | :--- |
| **00** | [**00-setup**](./00-setup/README.md) | Install Python, `ai-toolkit`, and `ComfyUI`. Downloads to recommended base models. |
| **01** | [**01-dataset-prep**](./01-dataset-prep/README.md) | Image curation guide and automated data cleaning and captioning scripts. |
| **02** | [**02-training**](./02-training/README.md) | Annotated `ai-toolkit` YAML configurations and execution instructions. |
| **03** | [**03-generating**](./03-generating/README.md) | Loading your LoRA into `ComfyUI`, setting weights, and running generation workflows. |

---

## Recommended System Specs & Performance

Training on a dedicated NVIDIA GPU is roughly **50x to 100x faster** than CPU execution. While CPU only mode is supported, running a full LoRA training job without CUDA hardware is generally impractical for standard workflows.

| Hardware | GPU VRAM | System RAM | Training Time | Usability |
| :--- | :--- | :--- | :--- | :--- |
| **Recommended** | 12GB VRAM (NVIDIA) | 32GB+ RAM | **~15 – 30 minutes** | Fast & Seamless |
| **Minimum** | 8GB VRAM (NVIDIA) | 16GB RAM | **~45 – 90 minutes** | Functional `--lowvram` |
| **CPU Only** | Multi-Core CPU | 32GB+ RAM | **24 – 72+ hours** | Extremely Slow |

--- 

## Responsible AI & Ethical Usage

`local-ai-replicator` is an open-source tool provided for educational, research, and creative use.

* **Consent & Likeness:** Only train models using your own datasets or subjects you have explicit permission to replicate.
* **Model Licenses:** Adhere to the terms and licensing of any underlying base checkpoints used.
* **Liability:** The author assumes no responsibility or liability for content generated with these local tools.

---

## License

This repository is licensed under the [Apache-2.0 License](LICENSE).
