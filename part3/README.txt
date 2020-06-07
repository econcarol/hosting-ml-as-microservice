How to deploy a lambda function (FaaS) using Google cloud?

(1) CMD: cd [the path to the folder that has main.py]
(2) CMD: gcloud functions deploy get_sentiment --runtime python37 --trigger-http
(3) test the model
(3a) CMD: curl https://[GCP_REGION-PROJECT_ID].cloudfunctions.net/get_sentiment -X POST -d "{\"review\":\"great movie!\"}" -H "Content-type: application/json" 
(3b) go to https://[GCP_REGION-PROJECT_ID].cloudfunctions.net/get_sentiment, add [?review=great+movie] to the end of the URL, hit enter
(4) You can delete the get_sentiment function from Google Cloud Platform after testing.