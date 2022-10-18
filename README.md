# Stable Diffusion Sandbox

Extenison to the Hackamatics 2021 project, which aimed to pull together all text2art resources and get it running on our GPUs.

Recently, text2art models have started to implement diffusion as part of their models, which have yielded some great results.

## Initial setup

```
# Setup environment and download models (one time only)
make env
source venv/bin/activate
make deps
make models
```

## Run text2art on Speechmatics GPUs

```
# grab GPU then run
qlogin -now n -pe smp 1 -q aml-gpu.q -l gpu=1 -pty y -N D_$(whoami)
cd ~/git/text2art && source venv/bin/activate
python3 -m text2art.vqgan.run --prompts "Three engineers hard at work during Hackamatics #artstation"
```

## Downloading Stable Diffusion Models

- Can be downloaded with Hugging Face Login at https://huggingface.co/CompVis/stable-diffusion-v-1-2-original
