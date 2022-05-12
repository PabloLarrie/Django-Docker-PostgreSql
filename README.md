Stores from different countries small example
=========================================================

## Coments:

* About me
* About this code
* Part 1 - Creating an API
* Part 2 - File Ingestion
* Part 3 - Running the code


## About me

I first met coding in November 2020. At that time, it started just being another hobby more. But slowly, I dedicated more and more time to the learning process. After that, I got inspired by a friend of mine to continue my learning with Django, and its related technologies. 
And after that, here I am. I don't have any kind of experience in the programming professional world, but at this time, I'm firmly committed to learning more and more about coding, and to endeavour to raise my skills as much as I can. I am very much looking forward to join the programming professional world, because I know that the time here will greatly increase the learning process. 


## About this code

I've created a Makefile, where I added the most common commands that I've been using. There, you will be able to see that there is a command named `setup`. You will need to use it if is the first time that you run this project.
If you'd rather work terminal, just use next instructions:

> docker-compose build

> docker-compose run api python manage.py migrate

> docker-compose run api python manage.py csv_ingestion


This should be enough. Keep in mind that when you have dependencies issues, you can run: 
> sudo chown `whoami` -R .


## Part 1 - Creating an API

* **Models:** This project has 4 different models: Country, Store, Manager, and CountryStores.
* **Serializers:** Regarding serializers, I decided to create one for each model that will have an endpoint. The FileWorks model serializer has a function to count how many works does that file has.
* **Views:** I also created two views. The first one will allow to show all files (list and detail). The second one is being used for both works and fileworks.
* **URLs:** After the views, I decided to create some nested urls.


## Part 2 - File Ingestion

 I've created a management command that can load the cvs into de database. You can run it with the Makefile (`Make charge_csv`) or by:
> docker-compose run api python manage.py csv_ingestion

Also, there is another one to flush the database to empty it (`Make empty_db`):
> docker-compose run api python manage.py flush

And there is another Makefile command just in case that you need to first, flush, and then, load the csv (`Make restart_db`).


## Part 3 - Running the code
To run the code it should be enough with:
> docker-compose up

After that, you can simpli check that everything works perfectly by checking the following links:

http://0.0.0.0:8000/countries/  
http://0.0.0.0:8000/countries/1/  
http://0.0.0.0:8000/countries/1/stores/  
http://0.0.0.0:8000/countries/1/stores/1/  

(Keep in mind that the integer value can be switched for another one)