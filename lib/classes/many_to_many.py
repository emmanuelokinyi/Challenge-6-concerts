class Band:
    
    def __init__(self, name, hometown, ):
        self._name = ""
        self.name = name
        self._hometown = ""
        self.hometown = hometown
        
        
        

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 1:
            self._name = name
        else:
            print('Name must be a non-empty string')

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, hometown):
        if isinstance(hometown, str) and len(hometown) > 1:
            self._hometown = hometown
        else:
            print('Hometown must be a non-empty string')
    
    @property
    def concerts(self):
        return [concert for concert in Concert.all if concert.band == self]

    def venues(self):
        if self.concerts:
            return list(set([concert.venue for concert in self.concerts]))
        return []

    def play_in_venue(self, venue, date):
        concert = Concert(date=date, band=self, venue=venue)
        return concert

    def all_introductions(self):
        introductions = []
        for concert in self.concerts:
            introduction = f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}"
            introductions.append(introduction)
        return introductions if introductions else None


class Concert:
    all = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            print("Date must be a non-empty string")

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value
        else:
            print("Band must be of type Band")


    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value
        else:
            print("Venue must be of type Venue")

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    def __init__(self, name, city):
        self._name = ""
        self.name = name
        self._city = ""
        self.city = city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            print("Name must be a non-empty string")

    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        if isinstance(city, str) and len(city) > 1:
            self._city = city
        else:
            print('City must be a non-empty string')

    def concerts(self):
        venue_concerts = [concert for concert in Concert.all if concert.venue == self]
        return venue_concerts if venue_concerts else None

    def bands(self):
        bands_set = set([concert.band for concert in self.concerts()])
        return list(bands_set) if bands_set else None

    def concert_on(self, date):
        for concert in self.concerts():
            if concert.date == date:
                return concert
        return None
