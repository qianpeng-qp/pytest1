class Restaurant ():
    """开店店"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print("打印店名："+self.restaurant_name)
    def open_restaurant(self):
        print("开张："+self.cuisine_type)
    def set_namber_served(self,number):
        self.number_served=number
        print("number_served"+str(self.number_served))
    def increment_number_served(self,devop_people):
        self.number_people += devop_people
