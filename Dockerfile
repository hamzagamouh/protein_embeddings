FROM python:3.7
# FROM conda/miniconda3
WORKDIR /app

COPY . .

# RUN conda create -n prot-embs python=3.7
# RUN conda run -n prot-embs \
#     && conda install pytorch torchvision torchaudio pytorch-cuda=11.7 cuda -c pytorch -c "nvidia/label/cuda-11.7.1" \
#     && pip install -r requirements.txt

RUN pip install -r requirements.txt


