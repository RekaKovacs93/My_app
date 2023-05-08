# Rock Paper Scissors
Let's settle this like adults


# ### SETUP ### #
Note: Every command needs Enter to be pressed in order to run.
**Installation necessary software(MAC)**
psycopg2 - https://pypi.org/project/psycopg2/
python - https://docs.python-guide.org/starting/install3/osx/
flask - https://phoenixnap.com/kb/install-flask
**Open the terminal**
1. Open the Spotlight Search (cmd + space bar)
2. Type "Terminal"
3. Press enter
**Creating a folder**
The terminal should start in ~ which is the home path.
4. Create a folder by pasting:
mkdir rock_paper_scissors
You can change the name as you see fit (e.g. mkdir foldername)
**Navigate to the folder**
Now you will need to step in to that folder
5. Navigate to the folder by pasting:
cd rock_paper_scissors
The ~ should now be showing 'project_daniel_dimoes'
**Setting up the GIT repository**
Once in the folder, create a GIT repository.
6. Initiate the Git repository by pasting:
git init
The 'rock_paper_scissors' should now have git:(main) in front of it.
**Accessing the files**
Still in the same folder
7. Pull (or access) the files by pasting:
git clone git@github.com:RekaKovacs93/My_app.git
**Creating the database**
8. Create the database by pasting:
    createdb rock_paper_scissors
This can be done from any point
**Generate the necessary tables**
9. Once the database has been created, generate the respective tables by pasting:
psql -d rock_paper_scissors -f db/rock_paper_scissors.sql
note: this needs to be ran from the parent folder of db (or the folder in which db is in), if this is not 'rock_paper_scissors' then follow below steps:
While in the folder project_daniel_simoes start by pasting:
ls
this should provide a list of all the items inside the folder rock_paper_scissors
if there is a folder inside that one you will need to navigate to that folder, you can do this by writing cd foldername.
**Running flask**
In order to run flask paste in to terminal:
flask run
