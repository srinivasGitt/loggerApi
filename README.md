Pip install requirements.txt

run 
uvicorn app.main:app --reload

Postman or Insomnia:
Method: POST
URL: http://localhost:8000/user/alice/activity
Body → raw → JSON:
{
  "event_type": "page_view",
  "timestamp": "2025-05-21T10:30:00Z",
  "metadata": {
    "page": "/dashboard",
    "browser": "Firefox"
  }
}

req body:
{
  "event_type": "page_view",
  "timestamp": "2025-05-21T10:30:00Z",
  "metadata": {
    "page": "/dashboard",
    "browser": "Firefox"
  }
}

response:
{
    "message": "activity recorded"
}


Curl (from terminal):
curl -X POST http://127.0.0.1:8000/user/alice/activity \
-H "Content-Type: application/json" \
-d '{
  "event_type": "form_submit",
  "timestamp": "2025-05-21T10:30:00Z",
  "metadata": {
    "page": "/form",
    "browser": "Edge"
  }
}'


