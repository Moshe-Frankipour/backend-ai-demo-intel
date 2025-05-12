# Backend AI Demo - Flask API with OpenAI

This project demonstrates how to set up and run a Flask API integrated with OpenAI.

## Prerequisites

- Python 3.8 or higher
- `pip` (Python package manager)
- OpenAI API key

## Setup Instructions

1. **Clone the Repository**
    ```bash
    git clone https://github.com/Moshe-Frankipour/backend-ai-demo-intel/
    cd backend-ai-demo-intel
    ```

2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set OpenAI API Key**
    Create a `.env` file in the project root and add your OpenAI API key:
    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

5. **Run the Flask Application**
    ```bash
    python -m flask run
    ```
    OR
    ```bash
    waitress-serve --listen=0.0.0.0:5000 app:app
    ```

6. **Access the API**
    Open your browser or API client and navigate to:
    ```
    http://127.0.0.1:5000
    ```

## Project Structure

```
backend-ai-demo-intel/
├── app.py             # Main Flask application
├── openai_client.py   # Openai Client
├── templates
    |- index.html      # Sample client
├── .github/workflows
    |- deploy.yml      # github workflow for deploy app
├── requirements.txt   # Python dependencies
├── .env               # Environment variables
└── README.md          # Project documentation
```

## Example API Usage

Send a GET request to the `/start` endpoint.
return session_id

Send a POST request to the `/agent/ask` endpoint with the following JSON payload:
```json
{
  "session_id": "XXXXXXX-XXXX-XXXX",
  "message": "Write a poem about AI."
}
```

Send a POST request to the `/generate` endpoint with the following JSON payload:
```json
{
  "prompt": "Write a poem about AI."
}
```

## License

This project is licensed under the MIT License.