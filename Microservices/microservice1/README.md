# 6156_Final_Project
This is the final project for COMS6156 Cloud Computing
## Set-up
### Installing
Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/fastapi-helloworld.git
```
### Create Virtual Enviornment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```
### Install FastAPI and Uvicorn
```bash
pip install fastapi uvicorn
```
### (Optional) Run Requirements.txt to install rest of the package
```
pip install -r requirements.txt
```

### Run FastAPI Server
```
uvicorn main:app --host 0.0.0.0 --port 8012
```
The server will start and listen on http://127.0.0.1:8012. You can access it in your browser or using a tool like curl:
```

curl -X POST http://127.0.0.1:8012/createpetowner \
-H "Content-Type: application/json" \
-d '{"Name": "John Doe", "Email": "john.doe@example.com", "Telephone": "1234567890", "State": "SomeState", "City": "SomeCity"}'
```
