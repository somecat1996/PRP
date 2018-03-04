import os


def start():
    os.system('openvassd')
    os.system('openvasmd')
    os.system('gsad')
    os.system('redis-server /etc/redis/redis.conf &')

if __name__ == '__main__':
    start()
