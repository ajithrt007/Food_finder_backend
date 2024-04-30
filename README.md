Installation
To run this project locally, follow these steps:

Prerequisites
Python (3.x recommended),
pip (Python package installer),,
Virtual environment (recommended),

Clone the Repository
git clone https://github.com/username/repository.git
cd repository

Setup Virtual Environment (Optional but Recommended)  
python -m venv venv  
venv/Scripts/activate (on Windows) # Activate the virtual environment  

Install Dependencies
pip install -r requirements.txt # Install required packages

Apply Database Migrations
python manage.py migrate

Start the Development Server
python manage.py runserver  
Now you can access the project at http://localhost:8000/.
