# Makefile for creating Sphinx documentation from modules in '../src'.
# Usage:
# - make html|docs      ; generate html-documentation
# - make clean          ; show files to clean-up
# - make clean-f        ; execute clean-up
# - make help           ; show help message (default)
#
# '?=' variables are set from the command line or from the environment.
PROJ_PATH   ?= ..
SRC         := $(PROJ_PATH)/src
DOCS_BUILD  ?= .
DOCDIR      := .
SPHINXOPTS  ?=
MAKEFLAGS += --no-print-directory   # disable messages when entering sub-dir

# first goal hit when 'make' is called with no goal provided as argument
help:
	@echo "Build Python project with make:"
	@grep '^# - make ' Makefile | sed 's/^.//'
	@sphinx-build -M help $(DOCDIR) $(BUILDDIR) $(SPHINXOPTS)

# create documentation using 'Sphinx'
docs: html
html: modules.rst
	sphinx-build -M html $(DOCDIR) $(DOCS_BUILD) $(SPHINXOPTS)
	@echo -e "\ncreated docs: $(DOCS_BUILD)/html/index.html" | sed -e 's!\.\./!!g'

# create module file used by 'Sphinx'
modules.rst:
	sphinx-apidoc -o $(DOCDIR) $(SRC)

# Show artifacts created during the build process to be cleaned-up
clean:
	@[ -z "$(MSG)" ] && echo "files to remove (remove with: 'make clean-f'):" || echo $(MSG) > /dev/tty
	@[ -f .keep ] && bash -c "find . $(shell cat .keep | sed '/^[[:space:]]*#/d' | tr '\n' ' ')"

# Execute clean-up
clean-f:
	@make clean MSG="removed:" | tee /dev/tty | xargs rm -rf

# Force goals to execute.
.PHONY: help docs html clean clean-f

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Manual 'Sphinx' build process:
# - cd docs (empty)
# - sphinx-quickstace and build directories (y/n) rt
#   - Separate sour[n]: n
#   - Project name: py-fun
#   - Author name(s): sgraupner
#   - Project release []: 1.0.0
#   - Project language [en]: en
# 
# - creates files:
#   - _build/
#   - _static/
#   - _templates/
#   - conf.py     <-- prepend: import sys, os // sys.path.insert(0, os.path.abspath('..'))
#                     fill in: extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']
#   - Makefile
#   - index.rst   <-- append: echo -e "\n   modules\n" >> index.rst
#   - make.bat    <-- remove
# 
# - run commands:
#   - sphinx-apidoc -o . ../src     <-- creates modules.rst, src.rst, ...
#   - make html     <-- creates: _build/html/index.html
#   - chrome _build/html/index.html
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
