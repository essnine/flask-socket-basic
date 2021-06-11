# Flask Socket Basic

I **don't** care if the name is grammatically incorrect.

Anyway. This is a simple Flask app. It needs Python 3.6+, and will not work with Internet Explorer (in case any of you are running ancient hardware).

The main app file implements a couple of API paths, the `/` path and `/chat`. The latter connects the page to a socketio instance on the server and emits a couple of events. The code is not too complicated to look at, and this project is a basic reference for students/trainees who want to learn about asynchronous concurrent communication and processing systems without getting their brains fried by the massive number of tutorials out there. (I also wanted to make something so simple it was self-describing and didn't need a video, but enough for anyone to clone and get started with using it.)

Anyway. Instructions.

1. clone the repo
2. create a virtualenvironment, being mindful of the python version required
3. `pip install requirements.txt`
4. `python app.py`
5. ????
6. profit(?)


ENV Configs so far are:
- FLASK_ENV: "development"
- SECRET_KEY: "secret!"

I have not included instructions for the environment file values you have to set. Figure that part out by yourself. I believe in you. 🙂
