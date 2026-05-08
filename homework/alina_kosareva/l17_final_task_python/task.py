import os
import re
import argparse


def parse_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to file or directory")
    parser.add_argument("-t", "--text", help="Text for search", required=True)
    return parser.parse_args()


def get_files(path):

    files = []
    if os.path.isfile(path):
        files.append(path)
    elif os.path.isdir(path):
        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            if os.path.isfile(full_path):
                files.append(full_path)

    return files


def read_logs(files):

    blocks = {}
    for file_path in files:
        current_time = None
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if re.match(r"^\d{4}-\d{2}-\d{2}", line):
                    current_time = line[:19]
                    blocks[current_time] = {
                        "file": os.path.basename(file_path),
                        "text": line,
                    }
                else:
                    if current_time:
                        blocks[current_time]["text"] += line

    return blocks


def search_text(blocks, search_text):

    for time, data in blocks.items():
        text = data["text"]
        if search_text.lower() in text.lower():
            found = True
            words = text.split()
            word_index = None
            for i, word in enumerate(words):
                if search_text.lower() in word.lower():
                    word_index = i
                    break
            if word_index is None:
                continue
            start = max(0, word_index - 5)
            end = word_index + 6
            result = " ".join(words[start:end])

            print("=" * 50)
            print(f"File: {data['file']}")
            print(f"Timestamp: {time}")
            print(f"Context: {result}")
            print("=" * 50)


args = parse_arguments()
files = get_files(args.path)
blocks = read_logs(files)
search_text(blocks, args.text)
