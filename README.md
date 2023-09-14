# Test assignment (Currency Converter)
Task: Develop a 'Currency Converter' service that operates via a REST API using any Python framework
## Prerequisites
Before you begin, make sure you have the following:
- Docker installed on your system.
## Setup
1. Clone this repository using following comand:
```sh
git clone https://github.com/Frostibums/test_task_KDA.git
```
2. Navigate to the project directory:
```sh
cd test_task_KDA
```
3. Change ***your-app-id-here*** with your actual APP_ID in **.env** file
4. Build the Docker image:
```sh
docker build . -t currency_converter:latest  
```
5. Run the Docker container:
```sh
docker run -p 7755:8000 currency_converter 
```
The Currency Converter API will be accessible at **http://localhost:7755** in your web browser.
## API Endpoints
You can use the **/api/rates** endpoint to convert currency. Here's how to use it:

- from: The currency code you want to convert from (e.g., USD, EUR).
- to: The currency code you want to convert to (e.g., GBP, JPY).
- value (optional): The amount you want to convert (default is 1.0).

Example Request:
```http
GET /api/rates?from=USD&to=RUB&value=1
```
Example Response:
```json
{
    "result": 62.16
}
```
## API Documentation
You can access the API documentation by navigating to [http://localhost:8000/docs](http://localhost:8000/docs) when the application is running locally. 
This interactive documentation provides details about the available API endpoints and request parameters.

