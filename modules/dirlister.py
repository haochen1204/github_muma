import os

def run(**args):
    '''
        获取当前目录的所有文件
    '''
    print("[*] In dirlister module.")
    files = os.listdir(".")

    return str(files)