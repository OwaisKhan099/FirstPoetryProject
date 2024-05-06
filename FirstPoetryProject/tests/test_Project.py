from firstpoetryproject import main
from fastapi.testclient import TestClient
from firstpoetryproject.main import app
def test_firstfunction():
    res = main.firstfunction()
    assert res=="Hello World"

def test_root_path():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code==200
    assert response.json() == {"Hello": "World"}
