#!/usr/bin/env python3
# encoding: utf-8

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def test():
    if request.method == 'GET':
        project_id = request.args.get('project_id', None)
        issue_id = request.args.get('issue_id', None)
        if not project_id or not issue_id:
            return json.dumps({'code': 404, 'reason': 'param error.'})
        
        return json.dumps(api_proxy.get_api_info(project_id, issue_id))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=('./secret.pem', './secret.key'))
