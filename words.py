#!/usr/bin/env python
"""
Retrieve and print words from a URL.

Usage:
    python words.py <URL>
    Ex: URL = http://sixty-north.com/c/t.txt

Note: This program is used by Pluralsight for there python course.
"""
from urllib import urlopen
import sys

def fetch_words(url):
    """
    Fetch a list of words from a URL.
    :param url:
        The URL of a UTF-8 text document.
    :return:
        A list of strings containing the words from the document.
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    return story_words


def print_items(items):
    """
    Print items one per line.

    :param items:
        An iterable series of printable items.
    :return:
    """
    for word in items:
        print(word)


def main(url):
    """
    Print each word from a text document from a URL.
    :param url:
        The URL of a UTF-8 text document.
    :return:
    """
    words = fetch_words(url )
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1]) # The 0th argument is the module filename