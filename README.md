# sage
#### Web Development Project on Citizen Science.<br>Ankit | Anas | Subrat

## Objective:
To create a web application which can perform following important task:
- User and Admin login
- Show images from backend database to logged in  User for **image tagging.**
- Logged in Admin user can accept the image tags validity and upload new images.

## Team Work:
- dbms-ctzs/sage will be our stable *mainline* repository.
- Please fork this repository to your own github account and work on the features you like.
- Give push to *mainline* when you feel some feature is complete. Inform everybody on chat, so that everyone can sync to it.

## Tools:
- Frontend: HTML, CSS, Javascript, Bootstrap.
- Backend: Django, Djangorest
- Database:

## Folder Structure:
- sage
     - frontend
     - backend

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
