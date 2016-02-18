# encoding=utf-8

__author__ = 'xiaowang'
__date__ = '18/2/16'


def read(file):
    with open(file) as f:
        x = f.readlines()



if __name__ == '__main__':
    file_path = '../.gitignore'
    read(file_path)

