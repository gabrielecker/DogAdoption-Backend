# encoding: utf-8
from views import dogs, breeds

urls = [
    ('/dogs/', dogs.DogAPI.as_view('dog_api')),
    ('/breeds/', breeds.BreedAPI.as_view('breed_api'))
]
