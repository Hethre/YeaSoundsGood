Install python

Install pip:
  sudo apt-get install python-pip

Install virtual env
  pip install virtualenv

Set up virtual env
  virtualenv venv --no-site-packages
  source venv/bin/activate

Install requirements
  pip install -r requirements.txt

To run:
  foreman start

Then hit http://0.0.0.0:5000

To push your changes
  git push origin master

To deploy live
  git push heroku master


An example .git/config

[remote "heroku"]
  url = git@heroku.com:soundsgood.git
  fetch = +refs/heads/*:refs/remotes/heroku/*
[remote "origin"]
  url = git@github.com:Hethre/YeaSoundsGood.git
  fetch = +refs/heads/*:refs/remotes/origin/*


To see what's in our hosted database:
Go to https://mongolab.com/databases/soundsgood
username: yeasoundsgooddev
password: yeas0undsg00d
