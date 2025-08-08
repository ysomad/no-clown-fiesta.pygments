# Aider

1. Set aider interpreter path
```sh
$ TOOL_PY=$(head -n 1 "$(which aider)" | cut -c 3-)
```

2. Install plugin using aider interpreter
```sh
"$TOOL_PY" -m pip install -e .
```

3. Check installation
```sh
"$TOOL_PY" - <<'PY'
from pygments.styles import get_style_by_name
print(get_style_by_name("no-clown-fiesta"))
PY
```

4. Use in aider:
```yaml
# .aider.conf.yml
code-theme: no-clown-fiesta
```
