# flappy bird

- Download git from https://git-scm.com/downloads/win

## Linux (Arch), macOS

```sh
git clone https://github.com/nhathuynguyen19/flappy-bird.git
cd flappy-bird
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Windows

```sh
git clone https://github.com/nhathuynguyen19/flappy-bird.git
cd flappy-bird
python -m venv venv
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
