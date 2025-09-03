✨ Story Writer LLM

Write witty, funny short stories in seconds using OpenAI’s GPT models
.
This project is a simple Python script that takes a prompt and generates a 5-sentence humorous story that’s family-friendly and easy to read.

📌 Features

🤖 Uses OpenAI GPT-4o to generate stories

📜 Stories are short, witty, and beginner-friendly

🔑 API key stored securely in a .env file

🖥️ Simple CLI script – run and get instant output

🚀 Getting Started
1. Clone the repository
git clone https://github.com/your-username/story-writer-llm.git
cd story-writer-llm

2. Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3. Install dependencies
pip install -r requirements.txt

4. Set up environment variables

Create a file named .env in the project root:

OPENAI_API_KEY=your_api_key_here

5. Run the script
python main.py

📝 Example Output
"Banana Business": "A monkey opened a fruit shop but only sold bananas. Customers kept asking for apples, so he painted bananas red. Everyone bought them thinking they were special apples. The town became obsessed with 'magic apples'. The monkey laughed all the way to the banana bank."

📖 Context: The funny part is that people were fooled by bananas painted red, showing how silly trends can be.

📂 Project Structure
story-writer-llm/
│── main.py              # Main script
│── requirements.txt     # Project dependencies
│── .env.example         # Example of environment variables
│── .gitignore           # Git ignored files
│── README.md            # Project documentation

⚡ Requirements

Python 3.8+

OpenAI Python SDK

python-dotenv
