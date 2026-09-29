import sys
import argparse
import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()
api_key = os.environ.get('OPENAI_API_KEY')
if not api_key:
    api_key=st.secrets["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)



def read_file(filename):
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"{filename} not found, check the file name")
        sys.exit(1)

def counter(content):
    word_count = dict()
    for word in content:
        word = word.lower().strip(".,?!")
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1

    lis = sorted(word_count.items(), key = lambda x : x[1], reverse= True)
    return lis[:3]

def summarize_text(content):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {
                "role" : "system",
                "content" : "You are an helpful assistance which provides short summary of the content"
            },

            {
                "role" : "user",
                "content" : f"please summarize following text {content}"
            }
        ],
        temperature= 0.3,
        max_tokens= 300
    )
    return response.choices[0].message.content


def main():
    # filename = "sample.txt"

    parser = argparse.ArgumentParser(description= "code for taking file parameter")
    parser.add_argument("filename", help = "Enter the name of the file here")
    parser.add_argument("--word_count", action = "store_true")
    args = parser.parse_args()
    content = read_file(args.filename)
    print(summarize_text(content))
    print(counter(content.split()))

    if args.word_count:
        print(f" Word Count : {len(content.split())}")
    else:
        print(f"{len(content.split())}")

if __name__ == "__main__":
    main()

