#!/usr/bin/env python3
import json
import sys
import os
from datetime import datetime

# parse args
dir_name = sys.argv[1]
if sys.argv[2] == 'verbose' or sys.argv[2] == '--verbose':
    verbose = sys.argv[2]
else:
    verbose = False

fout = open(dir_name + '/' + 'semantic_timeline.csv','w')
fout.write('startTime,endTime,locationName,address,confidence\n')

for subdir, dirs, files in os.walk(dir_name):
    for filename in files:
        if not filename.endswith('.json'):
            continue
        filepath = dir_name + '/' + filename
        with open(filepath) as f:
            # Load in Google Location History data.
            data = json.load(f)

        if verbose:
            print('Opening {}'.format(dir_name))

        

        if verbose:
            print('There are {} entries to look through'.format(len(data['timelineObjects'])))

        for entry in data['timelineObjects']:
            try:
                placeVisit = entry['placeVisit']
            except:
                if verbose:
                    # print('This entry has no "placeVisit" field.')
                    continue

            locationObj = placeVisit['location']
            locationName = locationObj['name'].replace('\n',' ').replace(',',' ')
            try:
                address = locationObj['address'].replace('\n',' ').replace(',',' ')
            except:
                if verbose:
                    print('Address not found.')
                address = ''
                
            confidence = locationObj['locationConfidence']

            durationObj = placeVisit['duration']
            # already determines local time?
            startTime = datetime.fromtimestamp(int(durationObj['startTimestampMs'])/1e3) # convert from ms to to seconds
            endTime = datetime.fromtimestamp(int(durationObj['endTimestampMs'])/1e3)

            fout.write('{},{},{},{},{}\n'.format(startTime,endTime,locationName,address,confidence))
            if verbose:
                print('Added entry: {} at {}'.format(startTime,locationObj['name']))

if verbose:
    print('Done')



    

    