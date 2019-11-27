#!/usr/bin/env python

import asyncio
import concurrent.futures
import requests

import asyncio
import concurrent.futures
import requests

async def main(number):

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:

        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor, 
                requests.get, 
                'http://127.0.0.1:8000/ping/'
            )
            for i in range(number)
        ]
        for response in await asyncio.gather(*futures):
            print(response.text)




if __name__ == '__main__':
    number = input("Enter the number of user: ") 
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(int(number)))





