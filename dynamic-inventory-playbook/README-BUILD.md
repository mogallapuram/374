# Q14 hints (homelab)

EE: `aap.cloud4ram.local/custom-ee-python:v1.0` (from q10). Tag must be lowercase `v1.0`.

```bash
chmod +x inventory/inventory*.py

# copy-playbook.yml
# ---
# - name: copy playbook with dynamic inventory
#   hosts: testing
#   become: true
#   tasks:
#     - name: copy file to testing server
#       ansible.builtin.copy:
#         content: "content from copy playbook"
#         dest: /tmp/copy-file.txt

ansible-navigator run copy-playbook.yml -i inventory \
  --eei aap.cloud4ram.local/custom-ee-python:v1.0 --pp missing -m stdout -v

# verify: ssh servera cat /tmp/copy-file.txt

git add . && git commit -m "q14" && git push
lab validate q14
```

(Exam question text sometimes mentions `/var/www/html/`; the worked example uses `/tmp/copy-file.txt` — this lab grades `/tmp/copy-file.txt`.)
