#! /usr/bin/env python

import json, csv, requests

def main():
    reader = csv.reader(open('../data/philadelphia-libraries/library-agsonline.csv', 'rb'))
    output_lines = ['address,lat,lon,zip']
    for row in reader:
        address = row[0]
        link = row[1].replace(' ', '%20')
        response = requests.get(link)
        dict = json.loads(response.content)
        candidate_dict = dict['candidates'][0]
        address_components = candidate_dict['address'].split(',')
        zip = address_components[len(address_components)-1].strip().replace('PA','')
        output_lines.append('%s,%f,%f,%s' % (address, candidate_dict['location']['y'], candidate_dict['location']['x'], zip))
        print candidate_dict['address']
    output_file = open('../data/philadelphia-libraries/libraries-geocoded.csv', 'w')
    try:
        output_file.write('\n'.join(output_lines))
    finally:
        output_file.close()
    print "Done"

if __name__ == '__main__':
    main()