from pathlib import Path
from multiprocessing import cpu_count

root_dir: Path = Path(__file__).resolve().parent
log_dir: Path = root_dir.parent / 'logs'
log_dir.mkdir(exist_ok=True)

capture_output: bool = True
assesslog: str = str(log_dir / 'gunicorn-access.log')
errorlog: str = str(log_dir / 'gunicorn-error.log')
loglevel: str = 'error'

bind: str = ':8000'
threads: int = 2
workers: int = cpu_count()
timeout: int = 60 * 5

reload: bool = False
name: str = 'sie_mpctl'
