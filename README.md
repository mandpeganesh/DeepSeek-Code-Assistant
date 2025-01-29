# DeepSeek Code Assistant

DeepSeek Code Assistant is a Django-based web application that provides an AI-powered coding assistant. It leverages the HuggingFace API to analyze user queries and provide accurate, detailed, and optimized coding solutions.

## Installation Instructions

### Prerequisites

- Python 3.8+
- Django 5.1.5
- A HuggingFace API token

### Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/deepseek_code_assistant.git
    cd deepseek_code_assistant
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required Python packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a [.env](http://_vscodecontentref_/0) file in the root directory and add your HuggingFace API token:

    ```env
    HUGGINGFACHUB_API_TOKEN=your_huggingface_api_token
    ```

5. **Apply database migrations:**

    ```sh
    python manage.py migrate
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:8000/
    ```

## Features

### User Interface

- **Modern UI:** The application uses Tailwind CSS for a modern and responsive design.
- **Syntax Highlighting:** Code blocks are highlighted using Prism.js for better readability.

### Functionality

- **AI-Powered Responses:** The application uses the HuggingFace API to provide AI-generated coding solutions.
- **Markdown Support:** Responses are rendered in Markdown with support for fenced code blocks.
- **Asynchronous Form Submission:** Queries are submitted asynchronously using JavaScript, providing a smooth user experience.

### Code Structure

- **Views:** The main logic for handling user queries is in [views.py](http://_vscodecontentref_/1).
- **Forms:** The [QueryForm](http://_vscodecontentref_/2) in [forms.py](http://_vscodecontentref_/3) handles user input validation.
- **Templates:** The HTML structure and design are defined in [home.html](http://_vscodecontentref_/4).
- **LangChain Integration:** The [langchain.py](http://_vscodecontentref_/5) file contains the logic for interacting with the HuggingFace API.

### Security

- **CSRF Protection:** The application includes CSRF protection for form submissions.
- **Environment Variables:** Sensitive information like API tokens are stored in environment variables.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
