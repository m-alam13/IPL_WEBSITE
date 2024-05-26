from src.flask_app import app
from src.db import CreateTables


if __name__ == "__main__":
    tables = CreateTables()
    app.run(debug=True,host='0.0.0.0', port=8000)
