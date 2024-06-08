<!-- Create the virtual environment using below command -->

1. python -m venv venv_name

<!-- Activate the virtual environment -->

2. cd venv_name/scripts
3. activate

<!-- Install the requirements -->

4. pip install -r requirements.txt

<!-- Navigate the application folder -->

5. cd ../../address_book

<!-- Run the application -->

6. uvicorn main:app --reload

<!-- Open the swagger and check the api's -->

7. http://127.0.0.1:8000/docs