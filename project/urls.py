# encoding: utf-8
from views import dogs, breeds, users

urls = [
    ('/dogs/', dogs.DogAPI.as_view('dog_api')),
    ('/breeds/', breeds.BreedAPI.as_view('breed_api')),
    ('/breed_dogs/', breeds.BreedDogsAPI.as_view('breed_dogs_api')),
    ('/users/', users.UserAPI.as_view('user_api')),
    ('/login/', users.LoginAPI.as_view('login_api')),
    ('/logout/', users.LogoutAPI.as_view('logout_api'))
]
