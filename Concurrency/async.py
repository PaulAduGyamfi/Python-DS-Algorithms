import asyncio, random, time

async def job_status(name: str):
    print(f"Getting Job[{name}]'s status ......")
    await asyncio.sleep(random.uniform(0.2, 1.5))
    return f"Job[{name}] : ran to completion"

sem = asyncio.Semaphore(2)

async def bound(name):
    async with sem:
        try:
            r = await asyncio.wait_for(job_status(name), timeout=1.0)
            print(f"Job[{name}]'s status retrieved!")
            return r
        except:
            print(f"Couldn't retrive Job[{name}] status : TimeoutError.")

async def main():
    t = time.perf_counter()
    results = await asyncio.gather(*[bound(f"t{i}") for i in range(5)], return_exceptions=True)
    print(results, f"{time.perf_counter()-t:.1f}s")

asyncio.run(main())