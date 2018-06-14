#! /usr/bin/python
import argparse
import json

def main():
    data = []
    output = ''
    parser = argparse.ArgumentParser(description='This program will create a comma-delimited string from a given input.')
    parser.add_argument('-q', action='store_true', default=False, help='Add quotes to each item')
    parser.add_argument('-l', action='store_true', default=False, help='Force lowercase')
    parser.add_argument('-d', action='store_false', default=True, help='Do not de-duplicate items')
    parser.add_argument('-p', action='store_true', default=False, help='Use | instead of , to separate values')
    parser.add_argument('-s', action='store_false', default=True, help='Do not sort items')
    args = parser.parse_args()
    quotes_on = args.q
    lower_case = args.l
    de_dupe_on = args.d
    pipe_on = args.p
    sorted_on = args.s
    print 'quotes_on='+str(quotes_on)
    print 'lower_case='+str(lower_case)
    print 'de_dupe_on='+str(de_dupe_on)
    print 'pipe_on='+str(pipe_on)
    print 'sorted_on='+str(sorted_on)
    while True:
        line = raw_input()
        line = str(line).strip()
        if line == '':
            break
        else:
            if lower_case == True:
                line = line.lower()
            if quotes_on == True:
                #line = json.dumps(line)
                line = '\"'+line+'\"'
            if de_dupe_on == True and line not in data:
                data.append(line)
            if de_dupe_on == False:
                data.append(line)
    if pipe_on == True:
        separator = '|'
    else:
        separator = ','
    if sorted_on == True:
        data.sort()
    output = separator.join(str(x) for x in data)
    print output
    
if __name__=="__main__":
    main()