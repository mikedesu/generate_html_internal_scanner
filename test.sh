#!/usr/bin/zsh

python3 main.py --payload xxx --ports $(python3 -c 'print(",".join([str(x) for x in range(0,23697)]))') > example.html

