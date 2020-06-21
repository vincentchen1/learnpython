#8-6. City Names
def city_country(city, country):
    location = f"{city}, {country}"
    return location

place = city_country('kaosiung', 'taiwan')
print(place.title())
place = city_country('san diego', 'usa')
print(place.title())
place = city_country('new york city', 'usa')
print(place.title())

#8-7. Album
def make_album(artist_name, album_name):
    album = f"{artist_name}, {album_name}"