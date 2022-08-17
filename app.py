from main.main import app, socketio
# from main.main import app, socketio
# import main

if __name__ == "__main__":
    # app.run(debug=True)
    socketio.run(app, debug=True)