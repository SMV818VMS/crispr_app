# CRISPR
## detection web application

--------------------

### Basic setup
```{bash}
git clone ssh://git@github.com/samiver/cripsr_app
cd cripr_app
virtualenv --python=python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

### Local server for development
```{bash}
source venv/bin/activate
python run.py
```
Now point your browser to **http://localhost:5000**

### Deployment
1. Do your changes locally, commit & `git push origin master`
2. Enter through ssh to the server & cd to the dir of the repository
3. `git pull origin master`
4. `sudo reboot`

----------------------

1. [Flask framework](http://flask.pocoo.org/)

2. [Modular Applications With Blueprints](http://flask.pocoo.org/docs/0.10/blueprints/)
