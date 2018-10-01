from django.shortcuts import render, redirect
from goodreads import client
import requests
from api_keys import key

# Create your views here.
def index(request):
    api_key = key['api_key']
    api_secret = key['api_secret']
    gc = client.GoodreadsClient(api_key, api_secret)
    first_book = gc.book(1)
    second_book = gc.book(2)
    third_book = gc.book(3)
    fourth_book = gc.book(4)
    fifth_book = gc.book(5)
    sixth_book = gc.book(6)
    seventh_book = gc.book(7)
    eigth_book = gc.book(8)
    ninth_book = gc.book(9)
    books = []
    print(gc)
    context = {
        'first_book': first_book,
        'second_book': second_book,
        'third_book': third_book,
        'fourth_book': fourth_book,
        'fifth_book': first_book,
        'sixth_book': sixth_book,
        'seventh_book': seventh_book,
        'eigth_book': eigth_book,
        'ninth_book': ninth_book,
    }
    return render(request, 'good_reads_api/index.html', context)