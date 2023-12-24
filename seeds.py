from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

# Setup SQLite in-memory database
engine = create_engine('sqlite:///one_to_many.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Create instances of Restaurant, Customer, and Review
restaurant1 = Restaurant(name='Restaurant A', price=3)
restaurant2 = Restaurant(name='Restaurant B', price=4)

customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Doe')

review1 = Review(restaurant=restaurant1, customer=customer1, star_rating=5)
review2 = Review(restaurant=restaurant1, customer=customer2, star_rating=4)
review3 = Review(restaurant=restaurant2, customer=customer1, star_rating=3)

# Add instances to the session
session.add_all([restaurant1, restaurant2, customer1,
                customer2, review1, review2, review3])

# Commit the changes to the database
session.commit()

# Close the session
session.close()
