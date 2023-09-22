import requests
import os 
import sys

AIERA_API_KEY = os.environ.get("AIERA_API_KEY")

# monitors
dashboard_guid = "e9a5c779145141ec8cdce2d52e9d919a" # replace with your monitor's id
stream_guid = "003ea7179bc94e4190dd56af5a3fe5f8" # replace with your stream guid

matches = requests.get(f"https://premium.aiera.com/api/dashboards/{dashboard_guid}/streams/{stream_guid}/matches?size=10", headers={"X-API-Key": AIERA_API_KEY})

if not matches.status_code == 200:
    print("Unable to complete request:")
    print(matches.text)
    sys.exit()


event_ids = [match["event"]["event_id"] for match in matches.json()["results"]]

# now we'll request transcripts for the events
# linguistics = true will return sentiment values for the transcript items

sentiment_results = []

for event_id in event_ids:
    res = requests.get(f"https://premium.aiera.com/api/events/{event_id}/transcript?linguistics=true", headers={"X-API-Key": AIERA_API_KEY})
    for transcript_result in res.json():
        sentiment_results.append(transcript_result["linguistics"]["sentiment"])

print(sentiment_results)

