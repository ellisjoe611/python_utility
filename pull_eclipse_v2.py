import asyncio
from asyncio.events import AbstractEventLoop
import os
import platform
import typing as T


async def pull(proj: str) -> int:
    print(f'[{proj}] pulling project now...')

    loop: AbstractEventLoop = asyncio.get_event_loop()
    res: int = await loop.run_in_executor(None, os.system, f'cd ./{proj} && git pull')
    return res

if __name__ == '__main__':
    print(platform.system().lower())
    if os.path.isdir('~'):
        os.chdir('~/eclipse-workspace')
    else:
        os.chdir('../eclipse-workspace')

    projects: T.List[str] = [proj for proj in os.listdir() if 'douzone-comet-' in proj]
    loop: AbstractEventLoop = asyncio.get_event_loop()

    group = asyncio.gather(*[pull(proj) for proj in projects])
    res = loop.run_until_complete(group)
    loop.close()

    print(f'\n\n----------RESULT---------\n{res}')
