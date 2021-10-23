import asyncio
from asyncio.events import AbstractEventLoop
import os
import time
import typing as T


def time_decorator(func):
    def __wrapper(*args, **kwargs):
        start: float = time.time()
        func(*args, **kwargs)
        end: float = time.time()
        print(f'function {func.__name__} took {end - start} seconds.')

    return __wrapper

async def pull(proj: str) -> int:
    print(f'[{proj}] pulling project now...')

    loop: AbstractEventLoop = asyncio.get_event_loop()
    res: int = await loop.run_in_executor(None, os.system, f'cd ./{proj} && git pull')
    if res == 0:
        print(f'[{proj}] complete pulling!')
    else:
        print(f'[{proj}] something went wrong while pulling...')

    return res

async def do_pull(co: T.Any, projects: T.List[str]):
    start: float = time.time()

    fs: T.List[T.Any] = [co(proj) for proj in projects if 'douzone-comet-' in proj]
    for f in asyncio.as_completed(fs):
        res = await f

    end: float = time.time()
    print(f'took {end - start} seconds.')


if __name__ == '__main__':
    if os.path.isdir('~'):
        os.chdir('~/eclipse-workspace')
    else:
        os.chdir('../eclipse-workspace')
    
    projects: T.List[str] = [proj for proj in os.listdir() if 'douzone-comet-' in proj]
    loop: AbstractEventLoop = asyncio.get_event_loop()

    loop.run_until_complete(do_pull(pull, projects))
    loop.close()
