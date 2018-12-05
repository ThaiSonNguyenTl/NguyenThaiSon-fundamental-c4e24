p1 = {
    "name": "Huy",
    "VND": 20,
    "hour": 25,
}
p2 = {
    "name": "Quan",
    "VND": 30,
    "hour": 30,
}
p3 = {
    "name": "Duc",
    "VND": 25,
    "hour": 15,
}
p_list = [
    {
    "name": "Huy",
    "VND": 20,
    "hour": 25,
    },
    {
    "name": "Quan",
    "VND": 30,
    "hour": 30,
    },
    {
    "name": "Duc",
    "VND": 25,
    "hour": 15,
    }
]
# cach nghi :xu ly mot cai trc
# sum = 0
# for p in p_list: #cho p chay tung phan tu p_list
    
#      name = p["name"] #truy cap vao name cua tung cai
#      vnd = p["VND"]
#      hour = p["hour"]
#      money = vnd * hour
#      print(name,money)
     
#      sum += money
# print(sum)
wage_list = [ p["VND"]* p["hour"] for p in p_list] #cach 
total = sum(wage_list)
print(wage_list)
print(total)