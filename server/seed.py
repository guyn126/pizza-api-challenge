from .app import create_app, db
from .models.restaurant import Restaurant
from .models.pizza import Pizza
from .models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    
    r1 = Restaurant(name="Mario's Pizza", address="123 Main St")
    r2 = Restaurant(name="Luigi's Pizza", address="456 Side Ave")
    r3 = Restaurant(name="Kiki's Pizza", address="789 Corner Blvd")

    
    p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    p3 = Pizza(name="Vegetarian", ingredients="Dough, Tomato Sauce, Cheese, Veggies")

    db.session.add_all([r1, r2, r3, p1, p2, p3])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=15, pizza_id=p2.id, restaurant_id=r1.id)
    rp3 = RestaurantPizza(price=8, pizza_id=p3.id, restaurant_id=r2.id)
    rp4 = RestaurantPizza(price=5, pizza_id=p1.id, restaurant_id=r3.id)

    db.session.add_all([rp1, rp2, rp3, rp4])
    db.session.commit()

    print("Database seeded!")
