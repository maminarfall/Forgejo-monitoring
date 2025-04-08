from flask import Flask, Response
from prometheus_client import generate_latest, Gauge

app = Flask(__name__)

repo_pushes = Gauge('forgejo_repo_pushes', 'Number of repository pushes')

@app.route('/metrics')
def metrics():
    repo_pushes.set(42)  # Replace with real data
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

#This exposes Forgejo metrics in Prometheus format.