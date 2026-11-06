E-Commerce Microservices Application

Project Overview

A simple e-commerce application built using Python Flask and a microservices architecture.

Architecture

The application consists of three independent microservices:

1. Product Service – Manages product information.
2. Cart Service – Adds products to the shopping cart and retrieves cart details.
3. Order Service – Creates orders, calculates total prices and maintains order history.

Technologies Used

- Python
- Flask
- REST APIs
- HTTP Requests
- PowerShell
- Git and GitHub

Service Ports

Service| Port
Product Service| 5001
Cart Service| 5002
Order Service| 5003

Features

- Retrieve product details.
- Add products to cart.
- Retrieve cart contents.
- Create customer orders.
- Calculate order totals.
- Retrieve order history.

Testing

APIs were tested using PowerShell Invoke-RestMethod.

Current Limitations

- Application data is stored in memory.
- Database integration is not yet implemented.
- Docker containerization and AWS deployment are pending.

Future Enhancements

- Integrate a database.
- Containerize services using Docker.
- Deploy services on AWS.
- Implement authentication and security.