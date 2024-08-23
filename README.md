# Clipboard AI Search

This script monitors the clipboard for new content and sends it to the GPT-4o-mini model for processing. The response is then copied back to the clipboard when `Ctrl+x` Pressed. Additionally, the script can be terminated using a hotkey (`Ctrl+B`).

## Prerequisites

- Python 3.6+
- OpenAI API Key
- Required Python packages: `openai`, `pyperclip`, `python-dotenv`, `keyboard`

## Installation

1. **Clone the repository**:

2. **Create and activate a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your OpenAI API key**:
    - Create a `.env` file in the root directory of the project.
    - Add your OpenAI API key to the `.env` file:
      ```env
      OPENAI_API_KEY=your_openai_api_key
      ```

## Usage

1. **Run the script**:
    ```sh
    python main.py
    ```

2. **Monitor the clipboard**:
    - The script will monitor the clipboard for new content.
    - When new content is detected, it will be sent to the GPT-4o-mini model for processing when  `Ctrl+x` Pressed.
    - The response will be copied back to the clipboard.

3. **Terminate the script**:
    - Press `Ctrl+B` to terminate the script.
