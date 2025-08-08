STYLE_NAME = no-clown-fiesta
PACKAGE_NAME = no-clown-fiesta-pygments
STYLE_FILE = no_clown_fiesta.py

TOOL_PY := $(shell head -n 1 "$(shell which aider)" | cut -c 3-)

.PHONY: install check uninstall

install:
	@echo "Using aider's Python: $(TOOL_PY)"
	@echo "Installing $(STYLE_NAME) theme for aider..."
	$(TOOL_PY) -m pip install -e .

check:
	@echo "Checking if $(STYLE_NAME) is installed..."
	@$(TOOL_PY) -c "import pygments.styles as s; print('no-clown-fiesta' in list(s.get_all_styles()))"

uninstall:
	@echo "Removing installed theme..."
	$(TOOL_PY) -m pip uninstall -y $(PACKAGE_NAME) || true
