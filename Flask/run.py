from Blog import create_app, db
import requests

app = create_app()

if __name__ == '__main__':
    print('-----Runing----------')
    db.create_all(app=app)
    app.run()
    # app.run(host='0.0.0.0', port=80)
    req = requests.get('http://127.0.0.1:4000')
    print(req.text)
    print(req.status_code)
