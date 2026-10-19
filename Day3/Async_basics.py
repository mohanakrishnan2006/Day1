import asyncio
import time
async def task(name,seconds):
    print(f"{name} is started")
    await asyncio.sleep(seconds)
    print(f"{name} is finished")
    return name

async def main():
    start=time.perf_counter()
    result=await asyncio.gather(
        task("A",4),
        task("B",2),
        task("c",5),
    )

    print(f"total time :{time.perf_counter() - start:.1f} seconds")


asyncio.run(main())
