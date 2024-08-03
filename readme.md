# google-timeline-parser

1. Download your timeline data from google Takeout

2. Locate the folder with the timeline data. It should have json files in it, similar to the following:
```
$ls Semantic\ Location\ History/2023
2023_APRIL.json   2023_DECEMBER.json  2023_JANUARY.json  2023_JUNE.json   2023_MAY.json       2023_OCTOBER.json
2023_AUGUST.json  2023_FEBRUARY.json  2023_JULY.json     2023_MARCH.json  2023_NOVEMBER.json  2023_SEPTEMBER.json
```

3. `python3 parse-timeline.py Semantic\ Location\ History/2024`
This generates a CSV file that's a bit easier to parse visually

4. Use the `location-query.py` and `wfh-checker.py` scripts to check how many work days you were at a location, including home. Syntax:
```
python3 location-query.py semantic-location-history/2023/semantic_timeline.csv "TARGET_ADDRESS_HERE"
python3 wfh-checker.py semantic-location-history/2023/semantic_timeline.csv "MY_ADDRESS_HERE" 
```
Don't forget to run these again for 2024 as well as 2023 (or whatever the financial year is.)
