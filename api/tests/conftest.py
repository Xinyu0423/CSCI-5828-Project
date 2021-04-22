from ... import app

@pytest.fixture
def app():
    app = app.create_app()
    return app