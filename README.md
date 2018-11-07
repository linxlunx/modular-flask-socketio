# Modular Flask SocketIO

## Overview
Flask socketio with blueprint implementation.

# Run
Install the requirements.
```
$ pip install -r requirements.txt
$ python run.py --help
Usage: run.py [OPTIONS]

Options:
  -i, --ip TEXT       Webservice Host  [default: 0.0.0.0]
  -p, --port INTEGER  Webservice Port  [default: 5000]
  --help              Show this message and exit.
$ 
```
Default will be running on http://localhost:5000, you can change the url and port in `config.py`, but you can also set host and port in the parameter.
```
$ python run.py 
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 183-895-598
(10187) wsgi starting up on http://0.0.0.0:5000
```

## Docker
### Docker build
Implemented with docker multistage build, so we could have smaller image size.
```
$ docker build . -t alpine:modular-flask-socketio
```

### Docker run
```
$ docker run -p 5000:5000 --rm -it alpine:modular-flask-socketio
```

### LICENSE

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
