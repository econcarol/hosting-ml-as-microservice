from flask import Flask, request
from predict_sentiment_analysis import get_sentiment
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # make cross-origin AJAX possible

@app.route('/', methods=['GET','POST'])
def predict():
	if request.method == 'GET':
		review = request.args.get('review') 
	else:
		review = request.get_json(force=True)['review']
	if not review:
		return 'No review found'
	
	result = get_sentiment(review)
	if result == 'pos':
		sentiment = 'Positive'
	else:
		sentiment = 'Negative'
	return sentiment

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False, host='0.0.0.0')
    # use the code below instead for Heroku deployment
    # port = int(os.environ.get('PORT', 5000)) 
    # app.run(debug=False, use_reloader=False, host='0.0.0.0', port=port)
