#!/usr/bin/env python3
# validate_wallet_schema.py (placeholder). Usa el script completo si quieres.
import json,sys
try:
  data = json.load(open('wallet-ticket-schema.json','r',encoding='utf-8'))
  print('JSON cargado. Estructura bÃ¡sica OK.')
  sys.exit(0)
except Exception as e:
  print('ERROR al parsear JSON:',e)
  sys.exit(1)
