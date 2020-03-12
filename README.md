# Upcoming Movies WebApp

This app is a solution to ArcTouch's hiring challenge.

You can access a **live demo** by [clicking here](https://upcominglistchallenge.pythonanywhere.com/).

## Architecture

This app uses Django/Python in the backend and Vue.js in the frontend.

We have two modules in this project, frontend and api.

The frontend module is where we have all the code related to the frontend part of the app. For that we have two vue apps, one for the list of the upcoming movies and another one. This is, also, where we have our static files, such as css, images, javascript and our html templates, where all data is displayed.

The api module our API layer and where we get data from the TMDB api and serve to our frontend app.

## Instalation

If you wish to run this on your local machine you should follow:

1. Clone this repo and navigate to its folder using the terminal.
2. Create a virtual environment, activate it and install the requirements:
  1. Create it by ` python3 -m venv myvenv `
  2. Activate it by ` . myvenv/bin/activate `
  3. Install or upgrade pip by ` python3 get-pip.py `
  4. Install the requirements by ` pip install -r requirements.txt `
3. Run the server: ` ./manage.py runserver`
4. Open your browser, go to ` 127.0.0.1:8000 ` and you should see the app running.
