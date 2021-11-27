from tests import meld_test_project
app = meld_test_project.create_app()


if __name__ == "__main__":
    app.run(port=5001)
