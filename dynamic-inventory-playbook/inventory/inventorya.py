#!/usr/bin/env python3
import json
import sys

INV = {
    "testing": {"hosts": ["servera.cloud4ram.local"]},
    "_meta": {"hostvars": {}},
}

if len(sys.argv) > 1 and sys.argv[1] == "--list":
    print(json.dumps(INV))
elif len(sys.argv) > 1 and sys.argv[1] == "--host":
    print(json.dumps({}))
else:
    print(json.dumps(INV))
