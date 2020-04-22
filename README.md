# sage
#### Web Development Project on Citizen Science.<br>Ankit | Anas | Subrat

## Instruction(towards becoming pseudo-professional)
0. Clone this repo using git clone better to clone it to your own repo and give pull requests.

1. Install pipenv which will be used later when deplyoing. pipenv creates a pipfile which locks dependencies, used for deplyment in webserver.
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
4. Plese inform the team when you push something here.

5. Use WIKI tab to share any detailed information having images/tables or it can be shared as details.pdf/details.doc etc

## Objective:
To create a web application which can perform following important task:
- User and Admin login
- Show images from backend database to logged in  User for **image tagging.**
- Logged in Admin user can accept the image tags validity and upload new images.

## Tools:
- Frontend: HTML, CSS, Javascript, Bootstrap.
- Backend: Django
- Database: Sqllite

## Folder Structure:
- sage
     - sage //project info file
     - manage.py
     - account //authentication
     - dashboard //dashboard

## Frontend:
1. **Logo and Name**
2. **Homepage**: 
     - Navbar
     - Text which will give user an idea of project.
     - Login
     - Tutorials of how to help
     - About us
3. **Users Dashboard:**  
    - Show image for image tagging.
    - Number of Submissions.
    - User profile Details.
    - User Ranking
4. **Admins Dashboard:**
    - Profile Details
    - Approval of Image tags.
    - Upload new images.

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
1. User Login and registration API (use simple forms for html templates- will be made beutiful later)
2. Create approproate tables-> models.py
3. User dashboard: show images and questions(no need to query database just use dummy image and data), decide whether to use AJAX call to serve image or server side generation of each page.
4. Handle image query from database(fetch image from database)(only database- it will be linked to above later)
5. User profile: show user profile to edit(show and query both)
6. Ranking: Show ranking of all users(no need to query database- use dummy data)
7. Query rank of user from database.
