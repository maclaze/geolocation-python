from geolocation.google_maps import GoogleMaps

if __name__ == "__main__":
    address = "Wall Street 12"

    google_maps = GoogleMaps(api_key='your_google_maps_api_key')

    location = google_maps.query(location=address)

    print(location.all())

    my_location = location.first()

    print(my_location.city)
    print(my_location.route)
    print(my_location.street_number)
    print(my_location.postal_code)

    for administrative_area in my_location.administrative_area:
        print("{}:{}".format(
            administrative_area.area_type, administrative_area.name))

    print(my_location.country)
    print(my_location.country_shortcut)

    print(my_location.formatted_address)

    print(my_location.lat)
    print(my_location.lng)
