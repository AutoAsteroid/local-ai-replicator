# Step 00: Environment Setup & Model Downloads

In this step, we will install `Python`, `ai-toolkit`, and `ComfyUI`, and download the base model checkpoints needed for training and inference.

---

## 1. Installing Python

Before running `ai-toolkit`, ensure **Python 3.12** is installed and properly configured on your system.

- **Recommended Version:** **Python 3.12.x** (Official recommendation for `ai-toolkit` and `PyTorch`)
- **Downloads:** [Official Python Releases](https://www.python.org/downloads/)
- **Important:** During installation, check the box that says **"Add Python to PATH"** before clicking Install.

## 2. Installing ai-toolkit

`ai-toolkit` by ostris is the open-source engine used to fine-tune LoRAs locally on your GPU.

1. Go to the official [ai-toolkit](https://github.com/ostris/ai-toolkit) GitHub Repository.
2. Click the green **`<> Code`** button near the top right and select **"Download ZIP"**.
3. Extract the downloaded ZIP file into any convenient folder on your PC (e.g., `C:\ai-toolkit\`).

## 3. Installing ComfyUI

`ComfyUI` is the visual node interface where you will load your trained LoRA to generate high-resolution images.

1. Go to the official [ComfyUI](https://github.com/comfyanonymous/ComfyUI/releases) GitHub releases page.
2. Download the **Portable Version** zip file for your system (e.g., `ComfyUI_windows_portable...`).
3. Extract the `.7z` or `.zip` file into any convenient folder on your PC (e.g., `C:\ComfyUI\`).

## 4. Downloading Base Models

To create high-fidelity images, you need a **base model checkpoint** (`.safetensors` file). Think of the base model as the "foundation" or "brain" that understands art styles, lighting, and real-world concepts, while your trained LoRA acts as a specialized patch or add-on layered on top.

### Download one (or more) of the following `.safetensors` base checkpoints:

| Model Name | Best Used For | Download Link |
| :--- | :--- | :--- |
| **CyberRealismXL** *(Default)* | Photorealistic portraits, natural skin texture, realistic lighting & subject accuracy | [HuggingFace](https://huggingface.co/cyberdelia/CyberRealisticXL) / [Civitai](https://civitai.com/models/129666/cyberrealism-xl) |
| **RealVisXL V4.0 / V5.0** | Hyper-detailed skin pores, sharp facial features, photographic portraits | [HuggingFace](https://huggingface.co/SG161222/RealVisXL_V4.0) / [Civitai](https://civitai.com/models/139562/realvisxl) |
| **Juggernaut XL v9** | Cinematic scenes, environments, dynamic lighting & versatile realism | [HuggingFace](https://huggingface.co/RunDiffusion/Juggernaut-XL-v9) / [Civitai](https://civitai.com/models/133005/juggernaut-xl) |
| **SDXL Base 1.0** | Official vanilla base model for broad, general-purpose training | [HuggingFace](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/sd_xl_base_1.0.safetensors) |

### Why I Recommend CyberRealismXL

Unlike corporate base models that are heavily safety-filtered and stylized, **CyberRealismXL** was fine-tuned on diverse, real-world photo datasets without artificial content restrictions. Because it retains full uncensored dataset awareness, it possesses a vastly deeper understanding of **human anatomy, natural body proportions, skin textures, and raw photographic lighting**. This makes it significantly more capable when learning custom subjects and generating realistic human figures without artificial censorship artifacts.
