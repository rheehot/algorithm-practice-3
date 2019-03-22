import os
import mmap
from dataclasses import dataclass

def read():
    '''
    stdin을 문제 스펙에 맞게 읽는 함수. stdin이 mmap(2)가 가능하지 않은 유형의
    파일인 경우 mmap(2)으로 파일을 읽는다.
    '''
    try:
        stdin = mmap.mmap(0, os.stat(0).st_size, mmap.MAP_PRIVATE, mmap.PROT_READ)
    except OSError as e:
        # mmap(2) 실패 이외의 이유로 실패했다면 예외 전파
        if e.errno != 22:
            raise

        # mmap(2) 가 불가능한 유형의 파일이여서 실패했다면 .read()로 입력 읽기
        count = int(input())
        yield from (int(word) for word in input().split())
        return

    # mmap(2) 활용하여 빠르게 입력 처리
    idx = stdin.find(b'\n')
    count = int(stdin[:idx])
    for _ in range(count):
        pos, idx = idx, stdin.find(b' ', idx + 1)
        yield int(stdin[pos:idx])

@dataclass(frozen=True)
class Seq:
    '''
    수열을 표현하는 자료구조. 길이와 수열의 맨 마지막 원소 정보만 들고있다.
    '''
    len: int
    last: int

def solution(numbers) -> int:
    sequences = set()
    for num in numbers:
        sequences |= {
            Seq(len=seq.len+1, last=num) for seq in sequences if seq.last < num
        } | {Seq(len=1, last=num)}
    return max(sequences, key=lambda e:e.len).len

if __name__ == '__main__':
    print(solution(read()))