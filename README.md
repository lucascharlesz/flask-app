# Flask Blog
## Requirements, installation and running the project
First things first, we need to install all the binaries, package managers, project dependencies, etc. In order to do so, in project\'s root folder run this command line:

## Python 3 and its package manager.
We're using Python 3. So, check if you have it installed:
* ` $ python3 --version `

If not, or you think it might be outdated, you can install or update the installtion running the following commands:
* ` $ sudo apt-get update `
* ` $ sudo apt-get install python3.6 `

We also need its package manager:
* ` $ sudo apt-get install python3-pip `

## After cloning the project

## Virtual Environment
We need to isolate the project's environment and install the dependencies in it. To do so, we create a *virtualenv*. To create your *virtualenv* run from the project's root directory in your terminal:
* ` $ python3 -m venv venv `

It might have created a **venv** directory in your project's folder.

Now, you already have installed all the Python 3 dependencies and created the environment.

We need to install the project's dependencies throught the package manager. First, activate the *virtualenv* you've just created:
* ` $ . venv/bin/activate `


## Project Dependencies
Then, you can install the dependencies:
* ` $ pip3 install -r requirements.txt `

Now, initialize the database:
* ` $ python manage.py db init `

Then, create its migrations:
* ` $ python manage.py db migrate --message 'initial database migration' `

After the migration, we need to apply it to the database:
* ` $ python manage.py db upgrade `

Now, you can simply run the server and you will be able to see the swagger documentation:
* ` $ python manage.py run `


## Opening in browser
If you open your browser at `localhost:5000` you might be able to see something like this:
<img src="https://cdn-images-1.medium.com/max/800/1*Us_S2WLR3AQAyfOvkzZ38Q.png" />

To make the server visible to the network run:
* ` $ python manage.py run --host=0.0.0.0 `

## Remember, when installing a lib or dependencie to your project, you might have activated the environment. If you don't, you will get in trouble.
To deactivate the environment, just run:
* ` $ deactivate `

## Running Tests
To run the tests, you might be able to simply run from your command line:
* ` $ python manage.py test `

You should see something like this:
<img src="https://cdn-images-1.medium.com/max/800/1*6_E40FN6IFz5EtwL1JqQTw.png"/>
