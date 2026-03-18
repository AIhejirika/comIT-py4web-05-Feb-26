import folium
import webbrowser
import math

# ========================
# BASE CLASS
# ========================
class Place:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def distance_to(self, other_place):
        lat_diff = self.latitude - other_place.latitude
        lon_diff = self.longitude - other_place.longitude
        return round(math.sqrt(lat_diff**2 + lon_diff**2) * 111, 2)

    def get_marker_color(self):
        return "blue"

    def get_popup_text(self):
        return f"<b>{self.name}</b>"

# ========================
# CHILD CLASSES
# ========================
class Restaurant(Place):
    def __init__(self, name, latitude, longitude, food_type):
        super().__init__(name, latitude, longitude)
        self.food_type = food_type

    def get_popup_text(self):
        return f"<b>RESTAURANT: {self.name}</b><br>Food: {self.food_type}"

    def get_marker_color(self):
        return "red"


class Park(Place):
    def __init__(self, name, latitude, longitude, has_playground):
        super().__init__(name, latitude, longitude)
        self.has_playground = has_playground

    def get_popup_text(self):
        playground = "Yes" if self.has_playground else "No"
        return f"<b>PARK: {self.name}</b><br>Playground: {playground}"

    def get_marker_color(self):
        return "green"


class Museum(Place):
    def __init__(self, name, latitude, longitude, entry_fee):
        super().__init__(name, latitude, longitude)
        self.entry_fee = entry_fee

    def get_popup_text(self):
        fee = "Free" if self.entry_fee == 0 else f"€{self.entry_fee}"
        return f"<b>MUSEUM: {self.name}</b><br>Entry: {fee}"

    def get_marker_color(self):
        return "purple"

# ========================
# MAP CLASS
# ========================
class MyMap:
    def __init__(self, city):
        self.city = city
        self.places = []
        self.map = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

    def add_place(self, place):
        self.places.append(place)
        folium.Marker(
            location=[place.latitude, place.longitude],
            popup=place.get_popup_text(),
            tooltip=place.name,
            icon=folium.Icon(color=place.get_marker_color())
        ).add_to(self.map)

    def show_distances(self):
        print("\nDistances:")
        for i in range(len(self.places)):
            for j in range(i+1, len(self.places)):
                p1 = self.places[i]
                p2 = self.places[j]
                print(f"{p1.name} → {p2.name}: {p1.distance_to(p2)} km")

    def save(self, filename="map.html"):
        self.map.save(filename)
        return filename

# ========================
# MAIN
# ========================
def main():
    mymap = MyMap("Paris")

    places = [
        Restaurant("Cafe Paris", 48.8566, 2.3522, "French"),
        Park("Luxembourg Garden", 48.8462, 2.3372, True),
        Museum("Louvre Museum", 48.8606, 2.3376, 17)
    ]

    for place in places:
        mymap.add_place(place)

    mymap.show_distances()

    file = mymap.save("my_map.html")
    webbrowser.open(file)

if __name__ == "__main__":
    main()