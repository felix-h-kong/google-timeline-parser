#!/usr/bin/env python3
import json
import sys
import os
from datetime import datetime

# parse args
dir_name = sys.argv[1]
verbose=True
# if sys.argv[2] == 'verbose' or sys.argv[2] == '--verbose':
#     verbose = True
# else:
#     verbose = False

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
            try: 
                locationName = locationObj['name'].replace('\n',' ').replace(',',' ')
            except:
                locationName = 'NO_LOCATION_NAME'
            try:
                address = locationObj['address'].replace('\n',' ').replace(',',' ')
            except:
                # if verbose:
                    # print('Address not found.')
                address = ''
                
            confidence = locationObj['locationConfidence']

            durationObj = placeVisit['duration']
            # already determines local time?
            # startTime = datetime.fromtimestamp(int(durationObj['startTimestampMs'])/1e3) # convert from ms to to seconds
            # endTime = datetime.fromtimestamp(int(durationObj['endTimestampMs'])/1e3)

            # they switched to using formatted strings (e.g. "2021-08-03T03:34:12Z") instead of POSIX time.
            # try to parse startTimestamp
            try: 
                startTime = datetime.strptime(durationObj['startTimestamp'],'%Y-%m-%dT%H:%M:%SZ') # no decimal places on the end
            except:
                try:
                    startTime = datetime.strptime(durationObj['startTimestamp'],'%Y-%m-%dT%H:%M:%S.%fZ') # has decimal places on the end
                except:
                    raise ValueError
            
            # try to parse endTimestamp
            try: 
                endTime = datetime.strptime(durationObj['endTimestamp'],'%Y-%m-%dT%H:%M:%SZ') # no decimal places on the end
            except:
                try:
                    datestr_format = '%Y-%m-%dT%H:%M:%S.%fZ'
                    endTime = datetime.strptime(durationObj['endTimestamp'],'%Y-%m-%dT%H:%M:%S.%fZ') #has decimal places on the end
                except:
                    raise ValueError

            fout.write('{},{},{},{},{}\n'.format(startTime,endTime,locationName,address,confidence))
            if verbose:
                print('Added entry: {} at {}, address: {}'.format(startTime,locationName, address))

if verbose:
    print('Done')



    

    