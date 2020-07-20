# sage
#### Web Development Project on Citizen Science.<br>Ankit | Anas | Subrat

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
3. Install dependencies: Pipfile has been updated sp run following:
```console
pipenv install
```
4. Inform other for any push. If on slack you will receive automatic update

## Dependencies(In case of error only. pipenv will handle all dependencies from pip.lock file)

1. To store jpeg/jpg/png images in database, install runtime library libjpeg8-dev in terminal by 
    ```console
    sudo apt-get install libjpeg8-dev
    ```
  and install python imaging library Pillow in terminal by    
    
     ```
      pip install Pillow  
     ```
    
2. To use social authentication for login, in terminal, install :
 
    ```console
        pip install python-social-auth[django]
    ```
 Also, register your app on Google Developer Console here : https://console.developers.google.com
 and after setup the Django-App, you will get the OAuth 2.0 Client ID and Secret Key which you need to write in settings.py     file.

 
 
3. Before starting the project, Do all migrations in terminal by:
 
    ```console
         python3 manage.py makemigrations
    ```
    and then
    
    ```console
        python3 manage.py migrate
    ```
4. Few other dependencies for Machine Learning Algorithms:
   
   ```
      pip install flask  
    ```
    ```
      pip install flask_cors  
    ```
    ```
      pip install joblib  
    ```
    ```
      pip install sklearn.externals  
    ```
    ```
      pip install newspaper  
    ```
    ```
      pip install newspaper3k  
    ```
    ```
       python3 -c "import nltk; nltk.download('all')" 
    ```
    ```
       python3 -c "import nltk; nltk.download('punkt')" 
    ```
    
  ## Machine Learning Dataset Information  
The dataset we will use for the fake news detection is called as "news.csv". This dataset has 7796. rows and 4 columns/ The first column identifies the news, the second and third are the title and text, and the fourth column has labels denoting whether the news is REAL or FAKE. The dataset can be downloaded from https://drive.google.com/file/d/1er9NJTLUA3qnRuyhfzuN0XUsoIC4a-_q/view
 
 -- Here, "app.py" file contains Flask APIs that receives news url through GUI or API calls, extracts the article from the url, feeds it to the model and returns the prediction.
 
 -- "fake_news_detection.py" contains code for our Machine Learning model to classify the news whether it is real or fake.
 
 -- Create the machine learning model by running below command -
     ```python fake_news_detection.py
     ```
This would create a serialized version of our model into a file model.pkl
 
 ## Exectution of Commands for ML Algorithm:   
 
 1) For UI   
    ```
      python manage.py runserver  
    ```
         
  Open the link url shown in terminal        
      
 2) For News Prediction   
    ```
      python app.py  
    ```
         
  Open the link url shown in terminal        
           
      

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
     - ctzs //project info file
     - manage.py
     - account //authentication

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
 
## Database Schema(PROPOSED)
Two databases are needed. Consider the example where user has to tag objects in images, in this case

0. PHOTO_TABLE = {primary_key = photo_id, image}
1. FINAL_TABLE = {primary_key = image_id,tags}
2. TAGGED_TABLE = {primary_key = image_id, tagged_or_not}
3. ITEMP_MAGE_TABLE = {primary_key=image_id,others columns will be attributes tagged by user,user_id,result}
     -Relation that stores the details filled by the user for the image along with the user_id.
     -Storing user_id here enables us to trace which user tagged the image.
     -result(attribute) - gives the status of whether image after being verified by administrator is ok or not.
4. USER_TABLE = Related to user statistics etc
     {primary_key = user_id,other attributes - no_tagged, good_tagged,bad_tagged,Rank..etc}
5. RANKING_TABLE - {primary_key: user_id,rank}
## How the database works     

- Initally all photos are inserted in the TAGGED_TABLE with tagged(attribute) as false.
- The user is shown photos from the TAGGED_TABLE images that have tagged(attribute) as false.
- After the user tags, the photo_id along with the tags is inserted into the TEMP_IMAGE_TABLE with verified(attribute) as false.
- The administrator verfies the tagged images in the TEMP_IMAGE_TABLE  and marks the result(attribute) as correct or wrong
- After the admin submits the result, if it was correct the tags for the photo tags of the photo_id will be updated in the FINAL_TABLE
     and the tagged attribute in the TAGGED_TABLE will be set as true. If it was wrong then nothing is done.
     The entry after the previous step is deleted from the TEMP_IMAGE_TABLE.
- After verification in the previous step, if the tagging was correct, the user statistics is updated in the USER_TABLE.
- This process is performed everytime a user requests an image
## Table Authorisation

User will not have access to the images he/she tags after they submit it.(This feature can be changed)
User will have access only to the RANKING_TABLE and USER_TABLE.
Admin has access to all tables.

## TODO
**(no need to work on authorization to each pages for now, login is only authenticated for now)**
**(use dummy image and dummy data when dbms query is not involved)**
1. Integration of web scraping and store in database
2. Fetch news article from database
3. Integrate ML API to news data
4. User Ranking profile.
5. User profile
