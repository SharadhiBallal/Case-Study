#!/usr/bin/env python
import requests as req

def main(number):
   for each in range(int(number)):
      resp = req.get("http://127.0.0.1:8000/ping/")
      print(resp.text)


if __name__ == '__main__':
    number = input("Enter the number of user: ") 
    main(number)
