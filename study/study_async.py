import time
import asyncio


async def find_users_async(n):
    for i in range(1, n + 1):
        print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
        # await asyncio.sleep(1)
    print(f'[{n}]')


async def process_async():
    start = time.time()
    await asyncio.wait([
        find_users_async(1),
        find_users_async(2),
        find_users_async(3),
        find_users_async(4),
        find_users_async(5),
        find_users_async(6),
    ])
    end = time.time()
    print(f'>>> 비동기 처리 총 소요 시간: {end - start}')

if __name__ == '__main__':
    asyncio.run(process_async())
