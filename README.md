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
