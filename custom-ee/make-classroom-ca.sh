#!/bin/bash
# Create classroom-ca.pem from AAP/Hub TLS cert (homelab stand-in for exam file).
set -euo pipefail
HOST="${1:-aap.cloud4ram.local}"
OUT="${2:-classroom-ca.pem}"
echo | openssl s_client -showcerts -servername "$HOST" -connect "${HOST}:443" 2>/dev/null \
  | openssl x509 -outform PEM > "$OUT"
echo "Wrote $OUT"
openssl x509 -in "$OUT" -noout -subject -issuer
