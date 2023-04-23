import sys
from os.path import exists
from header_reader import HeaderReader

file_name = sys.argv[1]

if exists(file_name):
    header_reader = HeaderReader(file_name)
else:
    raise RuntimeError(f'O arquivo {file_name} não existe. '
                       f'Verifique se o arquivo encontra-se na '
                       f'mesma pasta que o script.')

