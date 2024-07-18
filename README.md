# fastAPI_ASGI

**FastAPI as a Restaurant Kitchen**
FastAPI is like a super-efficient restaurant kitchen. The kitchen is FastAPI, recipes are the instructions (APIs) for making dishes, orders are what customers ask for (requests), chefs are the parts that handle specific requests (endpoints), and the menu is the automatic guide (documentation) showing what’s available and how to order. This way, customer requests are managed quickly and correctly, with clear instructions on what services are offered and how to use them.


![image](https://github.com/user-attachments/assets/c3402f67-ab29-46b7-9eb4-963ba62b2759)

**What is AGSI and the purpose of fastAPI in AGSI?**

ASGI stands for Asynchronous Server Gateway Interface, which allows multiple tasks to run concurrently. It's a specification for building asynchronous web applications and servers in Python.
In simple terms, FastAPI uses ASGI to build web APIs that can handle lots of requests at once, without slowing down. It's like having a kitchen that can cook many dishes simultaneously without anyone waiting too long for their food. This makes FastAPI great for applications where speed and efficiency are important, like handling multiple users accessing data or services online without delays.

**Server used: UVICORN**

Uvicorn is a lightning-fast ASGI server implementation that allows FastAPI (and other ASGI frameworks) to serve web applications. Think of it as the delivery service for your FastAPI kitchen: it takes the finished dishes (responses) from FastAPI and delivers them to the customers (clients) quickly and efficiently. Uvicorn is known for its speed and ability to handle many requests concurrently, making it an ideal companion for FastAPI when deploying web applications.


**API interacts with data with 4 main requests:** <br>
GET: Retrieve Data <br>
POST: Create Data <br>
PUT: Update Data <br>
DELETE: Delete Data



