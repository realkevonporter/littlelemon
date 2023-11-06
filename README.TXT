
Is the application set up with user registration and authentication?

    user registration
    http://127.0.0.1:8000/auth/users/

    user login
    http://127.0.0.1:8000/auth/token/login

    user logout
    http://127.0.0.1:8000/auth/token/logout


Does the web application use Django to serve static HTML content?
    simple static html page
    http://127.0.0.1:8000/restaurant/


Are the menu and table booking APIs implemented?

    menuAPI: 
    http://127.0.0.1:8000/restaurant/menu-items/

    bookingAPI: 
    http://127.0.0.1:8000/restaurant/booking/tables/ 

    authentication is required to test this endpoint. after authentication you can submit a payload
    to the bookingAPI like so: {"name": "Vonn","no_of_guests": 5,"booking_date": "2024-10-03"}

