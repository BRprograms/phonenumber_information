import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
phone_number=phonenumbers.parse("+6281317850827")
print(geocoder.description_for_number(phone_number,'en'))
print(carrier.name_for_number(phone_number,'en'))
