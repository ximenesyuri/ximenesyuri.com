SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = content
BUILDDIR      = dist
CONFDIR       = src

%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" -c "$(CONFDIR)" $(SPHINXOPTS) -v $(O)
            
build:
	@. .venv/bin/activate && \
	make clean && \
	make html && \
	rm -r dist/html/_sources && \
	rm -r dist/doctrees && \
	rm -r dist/html/search* && \
	rm -r dist/html/objects.inv && \
	rm -r dist/html/genindex.html && \
	rm -r dist/html/_static/alabaster.css && \
	rm -r dist/html/_static/basic.css && \
	rm -r dist/html/_static/custom.css && \
	rm -r dist/html/_static/doc* && \
	rm -r dist/html/_static/*.png && \
	rm -r dist/html/_static/*.svg && \
	rm -r dist/html/_static/*.js && \
	rm -r dist/html/_static/pygments.css && \
	mv dist/html/* dist && \
	rm -r dist/html && \
	deactivate
