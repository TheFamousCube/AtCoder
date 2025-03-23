from os import path, mkdir

mkdir('ABC')
for i in range(4):
    mkdir(f'ABC/{i}')
    for k in range(10):
        mkdir(f'ABC/{i}/{k}')
        for l in range(10):
            mkdir(f'ABC/{i}/{k}/{l}')
            for j in 'ABCDEFGH':
                open(f'ABC/{i}/{k}/{l}/{j}.py', 'w').close()