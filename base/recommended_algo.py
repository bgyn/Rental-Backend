import math

# using harvesine formula to calculate the distance 

def harvasine(lat1,lon1,lat2, lon2):
    R = 6371 # Earth radius on KM
    lat1,lon1,lat2,lon2 = map(float,[lat1,lon1,lat2, lon2])
    lat1,lon1,lat2,lon2 = map(math.radians,[lat1,lon1,lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c