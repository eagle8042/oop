class Toyota:

    brand = 'toyota'

    def __init__(self, color):
        self.color = color

rav4 = Toyota('black')
altis = Toyota('silver')

print(rav4.brand)
print(rav4.color)

print(Toyota.brand)

Toyota.brand = 'Ford'

print(rav4.brand)

rav4.brand = 'toyota'

print(altis.brand)
