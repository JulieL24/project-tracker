Feature	Points	What is done	                    Depends on
1	    5	    Install dependencies	
2	    7	    Set up the Django project and apps	1
3	    12	    The Project model	                2
4	    1	    Registering Project in the admin	3
5	    9	    The Project list view	            3
6	    2	    Default path redirect	            5
7	    10	    Login page	                        2
8	    3	    Require login for Project list view	5, 7
9	    4	    Logout page	                        7
10	    10	    Sign up page	                    2
11	    20	    The Task model	                    3
12	    1	    Registering Task in the admin	    11
13	    15	    The Project detail view	            12
14	    11	    The Project create view	            2
15	    13	    The Task create view	            11
16	    7	    Show "My Tasks" list view	        11
17	    11	    Completing a task	                16
18	    1	    Markdownify	                        17
19	    2	    Navigation	                        5, 7, 9, 10, 16

* [x] Fork and clone the starter project from Project Alpha Apr 
* [x] Create a new virtual environment in the repository directory for the project
* [x] Activate the virtual environment
  * [x] python -m venv .venv 
  * [x] source .venv/bin/activate
* [x] Upgrade pip
  * [x] python -m pip install --upgrade pip
* [x] Install django
  * [x] pip install django  
* [x] Install black
  * [x] pip install black
* [x] Install flake8
  * [x] pip install flake8
* [x] Install djhtml 
  * [x] pip install djhtml  
* [x] install debug toolbar
    * [x] pip install django-debug-toolbar  
* [x] Deactivate your virtual environment
  * [x] deactivate 
* [x] Activate your virtual environment
  * [x] source .venv/bin/activate
* [x] Use pip freeze to generate a requirements.txt file
  * [x] pip freeze > requirements.txt 
 * [x] create django project tracker
    * [x] django-admin startproject <<projectname>> .
* [x] create 3 apps accounts, projects, tasks  
    * [x] python manage.py startapp <<name>>
* [x] add app into settings.py installed app
  * [x] "<<name>>.apps.<<UppercaseName>>Config" 
* [x]run migrations
  * [x] python manage.py migrate  
* [x] create superuser 
  * [x] python manage.py createsuperuser 
* Feature 3
* [x] in projects app create Project model
  * [x] include name, description, members
  * Feature 4
* [x] Register Project model with the admin
  * Feature 5
* [x] create a list view for project model 
* [x] register the projects paths with tracker
  * [x] path "" and the name "list_projects" in projects.urls.py
* [x] create template for list view
* Feature 6
* [x] create a redirect view in tracker urls.py to redirect to project list
* Feature 7
* [x] Register the LoginView in accounts urls.py with "login/" path 
  * [x] Include url patterns form the accounts app in the tracker project with prefix "accounts/" 
  * [x] Create templates directory under accounts
  * [x] Create a registration directory under templates
  * [x] Create HTML template named login.html in the registration directory
  * [x] Put a post form in the login.html and other fundamental 5  
  * [ ] in the tracker settings.py create and set LOGIN_REDIRECT_URL to the value "home" 


## resources 
<https://learn-2.galvanize.com/cohorts/3352/blocks/1859/content_files/build/02-django-one-shot/65-django-one-shot-00.md>

<https://learn-2.galvanize.com/cohorts/3352/blocks/1859/content_files/build/03-django-two-shot/64-django-two-shot-reference-guide.md>

<https://learn-2.galvanize.com/cohorts/3352/blocks/1847/content_files/build/01-practice-and-project/66-assessment-project.md>

<https://docs.djangoproject.com/en/4.0/ref/models/fields/>

<https://docs.djangoproject.com/en/4.0/topics/auth/default/#all-authentication-views-1>