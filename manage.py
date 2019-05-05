from app import create_app

app = create_app('development' or 'default')

if __name__ == '__main__':
    app.run()
