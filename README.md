Code Generator Python

code-generator-python is a Python-based project for generating code, utilizing the Gemini API for advanced functionality.

Prerequisites

	•	Python Version: Python 3.12.7
	•	Pip Version: pip 23.3.2
	•	Gemini API Key:
Obtain your API key from Gemini AI Studio.

Setup Instructions

	1.	Clone the Repository

git clone <repository-url>
cd code-generator-python


	2.	Create a Virtual Environment

python -m venv venv


	3.	Activate the Virtual Environment
	•	On Windows:

.\venv\Scripts\activate


	•	If you encounter an error about execution policy, run:

Get-ExecutionPolicy

If it returns Restricted, update the policy:

Set-ExecutionPolicy RemoteSigned


	•	On MacOS/Linux:

source venv/bin/activate


	4.	Set Up API Key
	•	Create a .env file in the root directory where package.json exists.
	•	Add the following line with your Gemini API key:

GEMINI_API_KEY=*******


	5.	Install Dependencies

pip install -r requirements.txt


	6.	Run the Project

python run.py

Contributing

Feel free to fork the repository and create pull requests for any enhancements or bug fixes.

License

This project is licensed under [Insert License Name].
