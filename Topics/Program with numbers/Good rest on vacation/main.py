# put your python code here
duration = int(input())
daily_food = int(input())
flight_cost = int(input())
hotel_cost = int(input())

print((daily_food * duration) + (hotel_cost * (duration - 1)) + (flight_cost * 2))
