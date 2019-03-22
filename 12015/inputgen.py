from sys import argv, stdout
from random import Random

def dummy_input(count=1_000_000, seed=0):
    rng = Random(seed)
    yield from (
        rng.randrange(1, 1_000_001) for _ in range(count)
    )

if __name__ == '__main__':
    # 파라미터
    COUNT = int(argv[1]) if len(argv) > 1 else 1_000_000
    SEED = int(argv[2]) if len(argv) > 2 else 0

    # 실행
    print(COUNT)
    numgen = dummy_input(COUNT, SEED)
    stdout.write(f'{next(numgen)}')
    for num in numgen:
        stdout.write(f' {num}')
    stdout.write('\n')
