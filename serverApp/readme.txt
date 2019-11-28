1.Install Python
2. check if pip for python is installed. If not install it 
3.install all libraries in requirements.txt
	pip install -r requirement.txt

4. Install Redid for windows (run as service )
(Ref : https://github.com/MicrosoftArchive/redis/releases/download/win-3.0.504/Redis-x64-3.0.504.msi)

5.Run Server :
  python manage.py makemigrations server
python manage.py migrate
   python manage.py runserver 
6. To run simulator :
  python simulator.py
