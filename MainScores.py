from flask import Flask, request
from os import getenv
import Utils
import Score

app = Flask("WOG_SCORES")


def good_result(good_score):
    return '<html> \
                <head> \
                    <title>Scores Game</title>\
                </head>\
                <body>\
                    <h1>The score is <div id="score">{' + good_score + '}</div></h1>\
                </body>\
            </html>'


def bad_result():
    return '<html>\
                <head>\
                    <title>Scores Game</title>\
                </head>\
                <body>\
                    <h1><div id="score" style="color:red">{ERROR}</div></h1>\
                </body>\
            </html>'


@app.route('/scores', methods=['GET', 'POST', 'DELETE'])
def score(inp_score=0):
    try:
        inp_score=int(request.values['score'])
    except:
        None
    if request.method == 'POST':
        try:
            rc = Score.add_score(Utils.SCORES_FILE_NAME, inp_score)
            if rc == Utils.BAD_RETURN_CODE:
                raise ValueError("Wrong value")
            new_score = Score.get_score(Utils.SCORES_FILE_NAME)
            html_result = good_result(new_score)

        except:
            html_result = bad_result()

    elif request.method == 'GET':
        try:
            new_score=Score.get_score(Utils.SCORES_FILE_NAME)
            print (new_score)
            html_result = good_result(new_score)

        except:
            html_result=bad_result()
    elif request.method == 'DELETE':
        try:
            rc=Score.reset_score(Utils.SCORES_FILE_NAME)
            html_result = good_result("0")

        except:
            html_result=bad_result()
    return html_result


@app.route('/')
def my_func():
    return "hello and welcome to the world of games"


app.run(host="0.0.0.0", port=5001)
