from Blog import create_app, db
import requests

app = create_app()

if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=8080, debug=True)
    print('=====runing=========')
    app.run(host='0.0.0.0', port=80)
