<<<<<<< HEAD
def menu(item, quan, **restaurant):
    restaurant['Item'] = item
    restaurant['Quantity'] = quan
    return restaurant

restaurant = menu ('soup','1', Location='Seattle', Zipcode='98109')
=======
def menu(item, quan,  **restaurant):
    restaurant ['Item'] = item
    restaurant ['Quantity'] = quan
    return restaurant

restaurant = menu('soup', '1',Location ='seattle',Zipcode='98109')
>>>>>>> 7e78abe1b3c084e7a48e16a6d87e2ccaa8d3571e
print(restaurant)