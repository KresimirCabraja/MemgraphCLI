#Memgraph CLI

##Project setup:
On Ubuntu with Pipenv:

run
``pipenv install`` from root directory.
And after ``pipenv shell`` to activate virtual environment

or just run `./setup_env.sh` after you give it execution right with `chmod a+x setup_env.sh`.


##Commands:
First command:

``python3 main.py network --start_url=index.hr --depth=1
``


Second command:

``python3 main.py path --start_url=index.hr --end_url=https://www.index.hr/vijesti/clanak/
  veliko-istrazivanje-reutersa-hrvati-vijesti-najvise-prate-na-indexu/2285525.aspx
``

