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
 * [ ] create django project 
    * [ ] django-admin startproject <<projectname>> .
* [ ]run migrations
  * [] python manage.py migrate  
* [ ] create superuser 
  * [ ] python manage.py createsuperuser 
  * [ ] create 2 apps accounts and receipts 
    * [ ] python manage.py startapp <<name>>
* [ ] add app into settings.py installed app
  * [ ] "<<name>>.apps.<<UppercaseName>>Config"




## resources 
<https://learn-2.galvanize.com/cohorts/3352/blocks/1859/content_files/build/02-django-one-shot/65-django-one-shot-00.md>

<https://learn-2.galvanize.com/cohorts/3352/blocks/1859/content_files/build/03-django-two-shot/64-django-two-shot-reference-guide.md>

<https://learn-2.galvanize.com/cohorts/3352/blocks/1847/content_files/build/01-practice-and-project/66-assessment-project.md>

<https://docs.djangoproject.com/en/4.0/ref/models/fields/>

<https://docs.djangoproject.com/en/4.0/topics/auth/default/#all-authentication-views-1>