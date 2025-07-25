SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = content
BUILDDIR      = dist
CONFDIR       = src

%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" -c "$(CONFDIR)" $(SPHINXOPTS) -v $(O)

build-prod:
	make clean && \
	make html && \
	rm -r $(BUILDDIR)/html/_sources && \
	rm -r $(BUILDDIR)/doctrees && \
	rm -r $(BUILDDIR)/html/search* && \
	rm -r $(BUILDDIR)/html/objects.inv && \
	rm -r $(BUILDDIR)/html/genindex.html && \
	rm -r $(BUILDDIR)/html/_static/alabaster.css && \
	rm -r $(BUILDDIR)/html/_static/basic.css && \
	rm -r $(BUILDDIR)/html/_static/custom.css && \
	rm -r $(BUILDDIR)/html/_static/doc* && \
	mv $(BUILDDIR)/html/* $(BUILDDIR) && \
	rm -r $(BUILDDIR)/html
            
build:
	@. .venv/bin/activate && \
	make build-prod && \
	deactivate

serve:
	http-server $(BUILDDIR)/

up:
	make build && make serve
