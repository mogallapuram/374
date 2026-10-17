# Q9 build steps (homelab)

Exam-style: **you write** `execution-environment.yml` and `requirements.yml`.
See `*.yml.example` for a homelab reference (do not just rename blindly on the exam).

## 1. Write execution-environment.yml

Homelab (Hub often only has supported):

```yaml
---
version: 1
build_arg_defaults:
  EE_BASE_IMAGE: aap.cloud4ram.local/ee-supported-rhel9:latest
  EE_BUILDER_IMAGE: aap.cloud4ram.local/ee-supported-rhel9:latest
dependencies:
  galaxy: requirements.yml
```

Exam: use the **minimal** and **ansible-builder** image names from the question.

## 2. Write requirements.yml

```yaml
---
collections:
  - name: rhel-user-1.0.0.tar.gz
    type: file
```

Copy the tarball from q8 into this directory (match the filename/version).

## 3. Create classroom-ca.pem

```bash
echo | openssl s_client -showcerts -servername aap.cloud4ram.local \
  -connect aap.cloud4ram.local:443 2>/dev/null \
  | openssl x509 -outform PEM > classroom-ca.pem
# or: ./make-classroom-ca.sh
```

## 4. Create context and inject CA

```bash
rm -rf context
ansible-builder create
```

Edit **`context/Containerfile`** — under the first `USER root`, add:

```dockerfile
COPY classroom-ca.pem /etc/pki/ca-trust/source/anchors/
RUN update-ca-trust
```

```bash
cp classroom-ca.pem context/
cp rhel-user-*.tar.gz context/_build/
```

Homelab tip: if assemble fails on `systemd-python` (supported EE as builder), see comments in `Containerfile.example` / replace introspect+assemble with empty requirements.

## 5. Build, tag, push

```bash
podman login aap.cloud4ram.local
podman build -f context/Containerfile -t custom-ee-rhel-user-ca:v1.0 context
podman tag localhost/custom-ee-rhel-user-ca:v1.0 aap.cloud4ram.local/custom-ee-rhel-user-ca:v1.0
podman push aap.cloud4ram.local/custom-ee-rhel-user-ca:v1.0
lab validate q9
```
