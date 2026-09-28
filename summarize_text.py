import sys
import argparse

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

def main():
    # filename = "sample.txt"

    parser = argparse.ArgumentParser(description= "code for taking file parameter")
    parser.add_argument("filename", help = "Enter the name of the file here")
    parser.add_argument("--word_count", action = "store_true")
    args = parser.parse_args()
    content = read_file(args.filename)
    print(counter(content.split()))

    if args.word_count:
        print(f" Word Count : {len(content.split())}")
    else:
        print(f"{len(content.split())}")

if __name__ == "__main__":
    main()

