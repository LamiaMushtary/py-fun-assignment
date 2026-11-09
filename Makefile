# Makefile to build a basic Python project following the article by
# Ken Reitz: "Structuring Your Project",
# @see https://docs.python-guide.org/writing/structure
# 
# Usage:
# - make install        ; install/update packages from 'requirements.txt'
# - make run            ; run 'main.py' (default goal)
# - make tests          ; run tests (using 'pytest')
# - make docs           ; create docs in 'docs/_build/html'
# - make dist           ; run tests and package distribution in 'dist'
# - make clean          ; show files to clean-up
# - make clean-f        ; execute clean-up
# - make help           ; show help message (default)
# 
DIST = dist             # directory where distribution is packaged
DOCS = docs             # docs directory
DOCS_BUILD ?= $(DOCS)   # docs build-directory, either $(DOCS) or $(DIST)
ARTIFACT = $(DIST)/py_fun-1.0.0.tar.gz  # name/version in setup.py
REQUIREMENTS="requirements.txt"         # installation requirements
MAKEFLAGS += --no-print-directory       # disable msg when make enters sub-dir

# first goal hit when 'make' is called with no goal provided as argument
help:
	@echo "Build Python project with make:"
	@grep '^# - make ' Makefile | sed 's/^.//'

# run main.py
run:
	python -m main

# run tests using 'pytest', alternatively: python -m unittest -v tests
tests:
	pytest -v

# package source distribution in 'dist' using 'setup.py'
# - python setup.py sdist --dist-dir dist (deprecated)
# - python -m build --sdist --outdir dist
dist: clean
	pytest && \
		rm -rf $(DIST) && \
		mkdir -p $(DIST) && \
		python -m build --sdist --outdir $(DIST) && \
		make docs DOCS_BUILD=$(DIST) && \
		echo created artifact: $(ARTIFACT)

# build docs using 'sphinx' in 'docs' subdirectory
docs:
	@[ -d $(DOCS) ] && (cd $(DOCS); make docs DOCS_BUILD=../$(DOCS_BUILD)) || echo "no $(DOCS) directory"

# show artifacts created during the build process to be cleaned-up
clean:
	@[ -z "$(MSG)" ] && echo "files to remove (remove with: 'make clean-f'):" || echo $(MSG) > /dev/tty
	@[ -f .keep ] && bash -c "find . $(shell cat .keep | sed '/^[[:space:]]*#/d' | tr '\n' ' ')"

# execute clean-up
clean-f:
	@make clean MSG="removed:" | tee /dev/tty | xargs rm -rf

# install dependencies for the package from 'requirements.txt'
install:
	@pip install -r $(REQUIREMENTS) | grep -v "already satisfied" || \
		echo "everything from \"$(REQUIREMENTS)\" is up-to-date"

# goals forced to execute
.PHONY: help run tests dist docs clean clean-f install
