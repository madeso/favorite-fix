import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('files', metavar='file', nargs='+')
args = parser.parse_args()

total = 0
links = {}


def walk(b):
    global total
    global links
    name = b.get('title')
    uri = b.get('uri')
    if name is not None and uri is not None:
        print(name, uri)
        links[uri.lower()] = name
        total += 1
    children = b.get('children')
    if children is not None:
        for c in children:
            walk(c)

for fn in args.files:
    print fn
    with open(fn, 'r') as f:
        bookmarks = json.load(f)
        walk(bookmarks)

print total, len(links)