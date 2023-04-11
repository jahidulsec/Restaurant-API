# Restaurant API Project
## Description
In this project, Little Lemon API targeted to make it possible for your end-users to perform certain tasks and your reviewer will be looking for the following functionalities.

1. The admin can assign users to the manager group
2. You can access the manager group with an admin token
3. The admin can add menu items 
4. The admin can add categories
5. Managers can log in 
6. Managers can update the item of the day
7. Managers can assign users to the delivery crew
8. Managers can assign orders to the delivery crew
9. The delivery crew can access orders assigned to them
10. The delivery crew can update an order as delivered
11. Customers can register
12. Customers can log in using their username and password and get access tokens
13. Customers can browse all categories 
14. Customers can browse all the menu items at once
15. Customers can browse menu items by category
16. Customers can paginate menu items
17. Customers can sort menu items by price
18. Customers can add menu items to the cart
19. Customers can access previously added items in the cart
20. Customers can place orders
21. Customers can browse their own orders

## Run the project
To run this api,
- prepare virual environment
- install all the dependencies

Use the following commands.
```
cd LittleLemon

pipenv shell

pipenv install 

python manage.py makemigrations 

python manage.py migrate

python manage.py runserver 

```
### Browsing `menu-item` endpoint using the browser:
![menu item browsing endpoint screenshot](https://github.com/jahidulsec/Restaurant-API/1.png)

### Making an HTTP `GET` call to `menu-item` endpoint:
![HTTP `GET` call to `menu-item` endpoint screenshot](https://github.com/jahidulsec/Restaurant-API/2.png)

### Adding a user as a manager with admin token
![Adding a user as a manager with admin token](https://github.com/jahidulsec/Restaurant-API/3.png)

### The HTTP body content to add a user to the manager group with an admin token:
![add a user to the manager group with an admin token](https://github.com/jahidulsec/Restaurant-API/4.png)


## Credit
This project is a part of course work of APIs (Meta | Coursera). 
