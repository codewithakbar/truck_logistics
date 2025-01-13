import asyncio
import aiohttp
import time
from concurrent.futures import ThreadPoolExecutor

# Function to simulate blocking operations (for illustration)
def simulate_blocking_operation(data):
    return data

async def fetch_url(session, url, headers=None):
    """
    URL ga so'rov yuborish va javob olish funksiyasi.
    """
    start_time = time.time()
    try:
        async with session.post(url, headers=headers) as response:
            response.raise_for_status()  # agar xatolik bolsa uni chiqaradi
            response_json = await response.json()
            end_time = time.time()
            return end_time - start_time, response_json
    except aiohttp.ClientError as e:
        end_time = time.time()
        return end_time - start_time, {"error": str(e)}

async def fetch_with_threads(executor, session, url, headers=None):
    """
    Use ThreadPoolExecutor for blocking operations
    """
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, fetch_url, session, url, headers)

async def main(base_url="http://127.0.0.1:8090/lang/users/", num_requests=100):
    """
    Send multiple requests and measure their response times.
    """
    # Using ThreadPoolExecutor for blocking I/O operations (if needed)
    with ThreadPoolExecutor() as executor:
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_with_threads(executor, session, base_url) for _ in range(num_requests)]
            responses = await asyncio.gather(*tasks)

            # Process responses
            for idx, (response_time, response_json) in enumerate(responses):
                print(f"Javob vaqti {response_time:.4f}")
            print("-" * 50)
            print(f"Javob vaqti {response_time:.4f}")

if __name__ == "__main__":
    asyncio.run(main())
