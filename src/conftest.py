from . import server
import pytest
from threading import Thread


@pytest.fixture(scope='module', autouse=True)
def server_setup():
    isinstance = server.create_server()

    process = Thread(target=isinstance.serve_forever)
    process.setDaemon(True)

    process.start()