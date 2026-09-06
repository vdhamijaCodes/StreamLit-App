from dotenv import load_dotenv
load_dotenv()
import os
from openai import OpenAI
client  = OpenAI()
import sys
import argparse

def read_file(filename):
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"{filename} does not exists, check the current path")
        sys.exit(1)

def summarize_text(text):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {
            "role" : "system",
            "content"  : "You are a helpful assistance that provide the summary of a given text"
         },
         {
            "role" : "user",
            "content" : f"please summarize the following text \n\n {text}"
         }
        ],
         temperature= 0.3,
         max_tokens = 150
    )
    return response.choices[0].message.content


def count_words(text):
    dic = dict()
    for word in text:
        word = word.lower()
        if word in dic:
            dic[word] +=1
        else:
            dic[word] = 1

    counts = sorted(dic.items(), key = lambda x : x[1], reverse= True)
    return counts[:3]

def main():
    parser = argparse.ArgumentParser(description="Enter the name of the file")
    parser.add_argument("filename", help = "enter file name")
    parse = parser.parse_args()
    text = read_file(parse.filename)
    top = count_words(text.split('.,!?'))
    print(summarize_text(text)) 
    print("Top 3 words are :",top)

if __name__ == "__main__":
    main()


