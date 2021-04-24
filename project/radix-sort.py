import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_sort(arr, pos, max_length, n_buckets=128):
    sorted_arr = [None] * len(arr)
    occurances = [0] * n_buckets
    for word in arr:
        if max_length + pos - len(word) < 0:
            ch = word[pos + max_length] + 1
        else:
            ch = 0
        occurances[ch] += 1

    for i in range(len(occurances)-1):
        occurances[i + 1] += occurances[i]
    
    for i in range(len(arr)-1, -1, -1):
        word = arr[i]
        if max_length + pos - len(word) < 0:
            ch = word[pos + max_length] + 1
        else:
            ch = 0
        sorted_arr[occurances[ch] - 1] = word
        occurances[ch] -= 1

    return sorted_arr

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    words = book_to_words(book_url)

    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    pos = -1
    while pos + max_length >= 0:
        words = radix_sort(words, pos, max_length)
        pos -= 1
    
    return [i.decode('ascii') for i in words]
