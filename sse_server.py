from flask import Flask, Response
import time

app = Flask(__name__)

@app.route('/stream')
def stream():
    def event_stream():
        print('request received')
        start_time = time.time()
        elapsed_time = 0
        while elapsed_time < 60:
            yield 'data: {}\n\n'.format(time.ctime())
            time.sleep(1)  # Sleep for 1 second before sending the next event
            elapsed_time = time.time() - start_time

    return Response(event_stream(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
