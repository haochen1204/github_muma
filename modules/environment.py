import os

def run(**args):
    '''
        获取环境变量
    '''
    print("[*] In environment module.")
    return str(os.environ)
