
cab_fare = 852
wallet = 250
print(" can i book the cab",cab_fare <= wallet)
print(" can i book the cab",cab_fare >=wallet)


print(" can i book the cab",cab_fare ==wallet)

email ="Godfather@bmw.com"
password = "MODI_BC"
print("email auth:",(email == "Godfather@bmw.com"))
print("pass auth:",(password =="MODI_BC"))

print("user auth for home page:",(email == "Godfather@bmw.com") or (password =="MODI_BC"))

otp_sent = 1314
user_otp =int(input("enter OTP Received:"))

print("OTP MATCHED:",otp_sent ==user_otp)
is_internet_enables = True
is_GPS_enables = False
print("Can i Use App to login",is_internet_enables)
print("can i navigate using Google Maps",is_internet_enables and is_GPS_enables)

#Membership Testing

a = 10
print(a == 10)
print(a is 10)
print()
name = "amit banga"
print(name == "amit banga")
print(name is "amit banga")
print()
print(name == "ram")
print(name is "ram")
print()
print(name != "ram")
print(name is not "ram")
