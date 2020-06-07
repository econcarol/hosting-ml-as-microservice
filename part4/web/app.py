from flask import Flask, render_template, request
from predict_sentiment_analysis import get_sentiment

app = Flask(__name__)

@app.route('/')
def hello_whale():
    return render_template('whale_hello.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
	if request.method == 'GET':
		review = request.args.get('review') 
	else:
		review = request.get_json(force=True)['review']
	if not review:
		return 'No review found'
	return get_sentiment(review)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False, host='0.0.0.0')
