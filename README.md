# p3w3codechallenge
 Restaurant Review System
This application allows you to manage restaurants, customers, and their reviews.
Table of Contents
Introduction  - The Restaurant Review System is built using SQLAlchemy, a powerful and flexible Object-Relational Mapping (ORM) library for Python. This system manages three main entities: Restaurant, Customer, and Review. The relationships between these entities are defined to represent the interactions in a restaurant review domain
Setup - Clone the repository:
      -Install dependencies:
      -Apply database migrations:


Models:      
Restaurant -The Restaurant model represents a restaurant with a name, price level, and reviews.
Methods:
reviews(): Returns a collection of all the reviews for the restaurant.
customers(): Returns a collection of all the customers who reviewed the restaurant.
Customer - The Customer model represents a customer with a first name, last name, and reviews. 
Methods:
reviews(): Returns a collection of all the reviews that the customer has left.
restaurants(): Returns a collection of all the restaurants that the customer has reviewed.
Review - The Review model represents a review with a star rating, associated with a restaurant and a customer.
Methods:
customer(): Returns the Customer instance for this review.
restaurant(): Returns the Restaurant instance for this review.
full_review(): Returns a string-formatted review summary.
Object Relationship Methods - Ensure that relationships between Restaurant, Customer, and Review are correctly established.
Aggregate and Relationship Methods
Test and use aggregate methods such as full_name(), favorite_restaurant(), add_review(), delete_reviews(), and all_reviews().
Aggregate and Relationship Methods
