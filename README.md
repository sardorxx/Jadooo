

![logo.png](..%2FfastApiProject%2Flogo.png)
# Jadoo online market

Todo List

Python Base Section

1.Creating venv
1. Create and Activate venv
2. Create new github repository
3. Git clone empty repository with ssh or https

2.Creating Jadoo django project
1. Startproject
2. Startapp account, features and shop
3. Make models as structured
4. Makemigrations
5. migrate
6. Createsuperuser and check django as runserver

3.Creating Primary logics of website
1. Set up apps to base url and add to installed apps of django settings
2. Write main logic step by step to app view
3. App's views based on function
4. Each function must connect to urls of app

4.Creating extra files
1. Create extra_tools.py file to send email and remove background of product.image
2. Write signals.py to make same logic before save(pre_save) or after save(post_save)

* HTML, CSS and JS Base Section

1.Create some folders
1. Create templates folder for html
2. Create static folder css and js
3. Create media folder for image, mp3 and video

2.Create templates structure as understandable
1. Write template for account to login, signup, recover web page
2. Connect templates with app views, check is_connected
3. Write template for shop app to render products to web page
4. Connect templates with app views, check again for is_connected
5. Connect css files to html files
6. Check site for all section working correctly

* Testing with PyTest or UnitTest

1.Write tests
1. Write tests to every function and class of each app
2. Run each tests to check

* Built Project on Docker

1.Built Docker
1. Write Dockerfile and set up settings
2. Write docker-compose.yaml or docker-compose.yml file to built and run project

* Set up NGINX

1. Setup nginx.conf file to built project
2. Show static and media files on nginx

* To define some error setup github workflow

1. Create .github file in project
2. Create directory workflow and setup some settings to check which pushed source code 
3. Git Hub checks pushed code in its Actions section if code runs successfully, code will push else not.

* Deploying Website

1. Deploy website Digital Ocean or Amazon
2. Set UP remote server and then clone project from git hub repository

* Finally Site works correctly 

<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>

Result:

1.Home

![img_3.png](media%2FREADME_IMAGE%2Fimg_3.png)

2.Login Page

![img_03.png](media%2FREADME_IMAGE%2Fimg_03.png)

3.SignUp Page

![img_9.png](media%2FREADME_IMAGE%2Fimg_9.png)

4.Product Page

![img_4.png](media%2FREADME_IMAGE%2Fimg_4.png)

5.Side Bars

![img_5.png](media%2FREADME_IMAGE%2Fimg_5.png)

6.Product Detail

![img_6.png](media%2FREADME_IMAGE%2Fimg_6.png)

7.Top Products

![img_7.png](media%2FREADME_IMAGE%2Fimg_7.png)

8.Social Media

![img_8.png](media%2FREADME_IMAGE%2Fimg_8.png)

