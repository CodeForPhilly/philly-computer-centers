#! /usr/bin/env python

import json, re

def main():
    f = open('../data/freedom-rings/freedom-rings-pretty.json', 'r')
    try:
        content = f.read()
        center_list = json.loads(content)
        output_lines = []
        output_lines.append('name,address,lat,lon')
        for center in center_list:
            attributes = center['attributes']
            name = attributes['title'].replace('<br />','').replace('\n', ' ').replace(',', ' ')
            address = attributes['description'].replace('<br />','').replace('\n', ' ').replace(',', ' ')
            lat = float(attributes['field_goefield'])
            lon = float(attributes['field_goefield_1'])
            output_line = ('%s,%s,%f,%f' % (name, address, lat, lon)).replace('  ', ' ')
            output_lines.append(output_line)
        output_file = open('../data/freedom-rings/freedom-rings.csv', 'w')
        try:
            output_file.write('\n'.join(output_lines))
        finally:
            output_file.close()
    finally:
        f.close()

	print "Done"

if __name__ == '__main__':
	main()