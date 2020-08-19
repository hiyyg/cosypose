import cosypose
import os
import yaml
from joblib import Memory
from pathlib import Path
import getpass
import socket
import torch.multiprocessing
torch.multiprocessing.set_sharing_strategy('file_system')

hostname = socket.gethostname()
username = getpass.getuser()

PROJECT_ROOT = Path(cosypose.__file__).parent.parent
PROJECT_DIR = PROJECT_ROOT
DATA_DIR = PROJECT_DIR / 'data'
LOCAL_DATA_DIR = PROJECT_DIR / 'local_data'
TEST_DATA_DIR = LOCAL_DATA_DIR
DASK_LOGS_DIR = LOCAL_DATA_DIR / 'dasklogs'
SYNT_DS_DIR = LOCAL_DATA_DIR / 'synt_datasets'
BOP_DS_DIR = LOCAL_DATA_DIR / 'bop_datasets'

BOP_TOOLKIT_DIR = PROJECT_DIR / 'deps' / 'bop_toolkit_cosypose'
BOP_CHALLENGE_TOOLKIT_DIR = PROJECT_DIR / 'deps' / 'bop_toolkit_challenge'

EXP_DIR = LOCAL_DATA_DIR / 'experiments'
RESULTS_DIR = LOCAL_DATA_DIR / 'results'
DREAM_DS_DIR = LOCAL_DATA_DIR / 'dream_datasets'
DEBUG_DATA_DIR = LOCAL_DATA_DIR / 'debug_data'

DEPS_DIR = PROJECT_DIR / 'deps'
CACHE_DIR = LOCAL_DATA_DIR / 'joblib_cache'

assert LOCAL_DATA_DIR.exists()
CACHE_DIR.mkdir(exist_ok=True)
TEST_DATA_DIR.mkdir(exist_ok=True)
DASK_LOGS_DIR.mkdir(exist_ok=True)
SYNT_DS_DIR.mkdir(exist_ok=True)
RESULTS_DIR.mkdir(exist_ok=True)
DEBUG_DATA_DIR.mkdir(exist_ok=True)

ASSET_DIR = DATA_DIR / 'assets'
UR_DESCRIPTION = DEPS_DIR / 'ur5-description' / 'ur_description'
UR_DESCRIPTION_NEW = DEPS_DIR / 'ur5-description' / 'package_new_visuals' / 'ur_description'
OWI_DESCRIPTION = DEPS_DIR / 'owi-description' / 'owi535_description'
OWI_KEYPOINTS_PATH = DEPS_DIR / 'owi-description' / 'keypoints.json'

PANDA_DESCRIPTION_PATH = DEPS_DIR / 'panda-description' / 'panda.urdf'
PANDA_KEYPOINTS_PATH = DATA_DIR / 'dream' / 'panda_keypoints_infos.json'

CRAVES_YOUTUBE_RESULTS_DIR = DATA_DIR / 'craves-results/youtube-vis/preds'
CRAVES_LAB_RESULTS_DIR = DATA_DIR / 'craves-results/lab/preds'

MEMORY = Memory(CACHE_DIR, verbose=2)


CONDA_PREFIX = os.environ['CONDA_PREFIX']
if 'CONDA_PREFIX_1' in os.environ:
    CONDA_BASE_DIR = os.environ['CONDA_PREFIX_1']
    CONDA_ENV = os.environ['CONDA_DEFAULT_ENV']
else:
    CONDA_BASE_DIR = os.environ['CONDA_PREFIX']
    CONDA_ENV = 'base'

cfg = yaml.load((PROJECT_DIR / 'config_yann.yaml').read_text(), Loader=yaml.FullLoader)

SLURM_GPU_QUEUE = cfg['slurm_gpu_queue']
SLURM_QOS = cfg['slurm_qos']
DASK_NETWORK_INTERFACE = cfg['dask_network_interface']
