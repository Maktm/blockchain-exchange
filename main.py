"""

"""

import sys

from routes import app

# Web application configuration
host = '127.0.0.1'
port = 5000

header = """
  _____ ______   ___     __  __  _        ___  __ __    __  __ __   ____  ____    ____    ___ 
 / ___/|      | /   \   /  ]|  |/ ]      /  _]|  |  |  /  ]|  |  | /    ||    \  /    |  /  _]
(   \_ |      ||     | /  / |  ' /      /  [_ |  |  | /  / |  |  ||  o  ||  _  ||   __| /  [_ 
 \__  ||_|  |_||  O  |/  /  |    \     |    _]|_   _|/  /  |  _  ||     ||  |  ||  |  ||    _]
 /  \ |  |  |  |     /   \_ |     \    |   [_ |     /   \_ |  |  ||  _  ||  |  ||  |_ ||   [_ 
 \    |  |  |  |     \     ||  .  |    |     ||  |  \     ||  |  ||  |  ||  |  ||     ||     |
  \___|  |__|   \___/ \____||__|\_|    |_____||__|__|\____||__|__||__|__||__|__||___,_||_____|
                                                                                              
"""


def init() -> None:
    """Initializes the web application and starts the processing loop."""
    sys.stdout.write(header)
    sys.stdout.write('[+] Initializing web application ...\r\n')
    sys.stdout.write('[+] Warning: Please make sure that no other services are using {}:{}\r\n\r\n'.format(host, port))

    app.run(host=host, port=port)


if __name__ == '__main__':
    init()
