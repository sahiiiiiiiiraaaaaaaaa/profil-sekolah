import phonenumbers
from phonenumbers import carrier,
geocoder, timezone

mobileNo = input("masukkan nomor : ")
mobileNo = phonenumbers.parse(mobileNo)

#mendapatkan lokasi
print(timezone.time_zone_for_number)
(mobileNo)

#mendapatkan providor
print(carrier.name_for_number)
(mobileNo, "en")