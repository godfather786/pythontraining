restaurant = {
    "name":"jai shri bala ji",
    "reviews" : 4.7,
    "categories" : ["Mithai","Indian","Bakery","Fast Food"],
    "time to deliver" : 35,
    "price per person" : 150,
    "promo code": "shribala786"
}
restaurant["address"] ="civil lines"
restaurant["phone"] ="8013651414"

print(restaurant)
print(type(restaurant))
print(len(restaurant))
dish1 ={
     "name":"milk cake",
     "price":200
 }
dish2 = {
    "name": "barfi",
    "price": 150
}
dish3 ={
     "name":"coclate barfi",
     "price":250
 }
dishes =[dish1,dish2,dish3]
restaurant["dishes"]=dishes
print("RESTAURANT")
print(restaurant)
