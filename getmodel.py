import os
os.system('pip install requests huggingface_hub')
from huggingface_hub import hf_hub_download
repo=input('Repo ID:')
filedir=input('File Directory:')
hf_hub_download(repo_id=repo, filename=filedir)