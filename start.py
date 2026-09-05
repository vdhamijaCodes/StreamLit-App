# import sys
# import argparse

import json

# def read_file(filename):
#     try:
#         with open(filename, "r", encoding = "utf-8") as file:
#             return file.read()
#     except FileNotFoundError:
#         print("Filename {f} does not exists".format(f = filename))
#         sys.exit(1)

# def counter(counted):
#     counts = {}
#     for word in counted:
#         word = word.strip('.,!?').lower()
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1

#     counts = sorted(counts.items(), key = lambda x: x[1], reverse=True)
#     return counts[:3]

# def main():
#     parser = argparse.ArgumentParser(description="This is file reading progrea")
#     parser.add_argument("filename", help = "testing ground")
#     parser.add_argument("statement", help = "testing ground")
#     parser.add_argument("--verbose",action="store_true", help = "Show a labelled output") # use -- in case a variable must be made temporary
#     args = parser.parse_args()
#     print(args.statement)
#     content = read_file(args.filename)
#     if args.verbose:
#         print("word count :",len(content.split()))
#     else:
#         print(len(content.split()))

#     print("Top 3 most used words : ", counter(content.split()))

# if __name__ == "__main__":
#     main()


# def word_count(text):
#     return len(text.split())


# def main():
#     text = "hello world this is a python code"
#     print(word_count(text))

import json
import os
# def read_json(file_name):
#     with open(file_name,"r",encoding="utf-8") as file:
#         data = json.load(file)
#         return data

# def main():
#     file_name = "fake_response.json"
#     data = read_json(file_name)
#     print(data['content'][0]['text'])

def main():
    key = os.environ.get("MYFAKEKEYs")
    print(key)
   
if __name__ == "__main__":
    main()

hello world

Another change for testing

