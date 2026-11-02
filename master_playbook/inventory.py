#!/usr/bin/env python3
import json,sys
INV = {'testing': {'hosts': ['servera.cloud4ram.local']}, 'backend': {'hosts': ['serverb.cloud4ram.local']}, '_meta': {'hostvars': {}}}
print(json.dumps({} if "--host" in sys.argv else INV))
