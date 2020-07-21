# sage
### Live on: https://sage-citizen.herokuapp.com
#### Web Development Project on Citizen Science.<br>Ankit | Anas | Subrat
#### Indian Statistical Institute, Kolkata

## Instruction
0. Clone this repo using git clone and push updates at the end of a day..

1. Install pipenv which will be used later when deployoing. pipenv creates a pipfile which locks dependencies, used for deployment in webserver.
    ```console
    pip3 install pipenv
    ```
2. Run pipenv: It will take to it's shell
    ```console
    pipenv shell
    ```
3. Install dependencies: Pipfile/requirements.txt has been updated so run ANY ONE command of following:
    ```console
    pipenv install
    pip install -r requirements.txt
    ```
4. The folder 'ctzs' is the project folder. Run everything from that directory
    ```console
    cd ctzs
    ```

## Dependencies: (In case of error only) as pipenv will handle all dependencies from 'pip.lock' file.
0. Install dependencies using file 'requirements.txt'

1. To store jpeg/jpg/png images in database, install runtime library libjpeg8-dev and install python imaging library Pillow in terminal by:
    ```console
    sudo apt-get install libjpeg8-dev
    pip install Pillow  
    ```   

2. (opional) To use social authentication for login, also, register your app on Google Developer Console here : https://console.developers.google.com and after setup the Django-App, you will get the OAuth 2.0 Client ID and Secret Key which you need to write in settings.py file.:
    ```console
    pip install python-social-auth[django]
    ```

3. Before starting the project, do all migrations in terminal by:
    ```console
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
    
4. Dependencies for Machine Learning Algorithms:
   
    ```console
    pip install flask, flask_cors, jonlib, sklearn, newspaper3k
    pip install sklearn.externals
    python3 -c "import nltk; nltk.download('all')"
    python3 -c "import nltk; nltk.download('punkt')"
    ```
  
## Execution of Web Application:   
 
 1) For user interface, run following command and open the link url shown in terminal(127.0.0.1):
    ```console
    cd ctzs
    python manage.py runserver  
    ```       
      
 2) For news prediction involving Machine-Learning algorithm:   
    ```console
    cd ctzs
    python app.py  
    ```  
      
## Objective:
To create a web application which can perform following important task:
- User and Admin login
- Show news text from backend database to logged in  User for classifying it as Fake or Real
- API point to check validity of news

## Tools:
- Frontend: HTML, CSS, Javascript, Bootstrap.
- Backend: Django
- Database: Sqlite

## Folder Structure:
- sage
     - ctzs 
     - manage.py //to run application
     - account
     - app.py //for ML Algorithm
- webscrapping
- project_snapshots

## Frontend:
1. **Homepage**: 
     - Navbar
     - Text which will give user an idea of project.
     - Login
     - Tutorials of how to help
     - About us
2. **Users Dashboard:**  
    - Show news for classifying.
    - Number of Submissions.
    - User profile Details.
    - User Ranking


## Backend:
Here are API points and their functions.
1. **Authentication API:**
2. **User Interaction API**:
3. **Admin Interaction:**
4. **Database Tables:**

## Machine Learning Dataset Information  
The dataset we will use for the fake news detection is called as "news.csv". This dataset has 7796. rows and 4 columns/ The first column identifies the news, the second and third are the title and text, and the fourth column has labels denoting whether the news is REAL or FAKE. The dataset can be downloaded from https://drive.google.com/file/d/1er9NJTLUA3qnRuyhfzuN0XUsoIC4a-_q/view
 
 -- Here, "app.py" file contains Flask APIs that receives news url through GUI or API calls, extracts the article from the url, feeds it to the model and returns the prediction.
 
 -- "fake_news_detection.py" contains code for our Machine Learning model to classify the news whether it is real or fake.
 
 -- Create the machine learning model by running below command -
     ```python fake_news_detection.py
     ```
This would create a serialized version of our model into a file model.pkl     

## TODO
1. Integration of web scraping and storage in database
2. Integration ML API to news database
3. Activation of "Fake" and "Real" buttons
4. Limit comments to particular news article
5. Store userid, fake/real count per news articles
6. User Ranking profile.
7. User Profile
8. Add tutorial on home page

### Project report is included for reference. Everybody is welcome to team "sage" for contributions.
