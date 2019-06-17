from app import create_app

if __name__ == '__main__':
    app = create_app("development")
    print(app.url_map)
    app.run()
















