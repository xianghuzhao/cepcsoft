from bsm.util import safe_mkdir

from bsm.loader import load_relative
call_and_log = load_relative('util', 'call_and_log')

def run(param):
    version = param['pkg_info']['config']['version']
    url = param['action_param']['url'].format(version=version)
    dst_dir = param['pkg_info']['dir']['download']

    safe_mkdir(dst_dir)

    cmd = ['curl', '-v', '-f', '-L', '-s', '-S', '-R', '-O', url]
    with open(param['log_file'], 'w') as f:
        ret = call_and_log(cmd, log=f, cwd=dst_dir)

    return ret==0
