#!/usr/bin/env python

import sys
import json

if __name__ == '__main__':
    try:
        with open('resources/image-context.json', 'rb') as context:
            obj = json.load(context, 'UTF-8')
            print obj
    except IOError as e:
        sys.exit('Invalid context file: ' + e.message)
