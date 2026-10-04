TEX_FILES := $(wildcard preparatory/*.tex task_reports/*.tex)
PDF_FILES := $(TEX_FILES:.tex=.pdf)
BIB_FILE := ../research/contract-design/references.bib

.PHONY: all list clean

all: $(PDF_FILES)

preparatory/contract_design_preparation.pdf: ../research/contract-design/figures/step2_liquidity_four_panel.pdf

list:
	@printf '%s\n' $(TEX_FILES)

preparatory/%.pdf: preparatory/%.tex templates/shared.tex $(BIB_FILE) Makefile
	mkdir -p .build/preparatory/$*
	cd .. && latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=intermediate/.build/preparatory/$* intermediate/preparatory/$*.tex
	cp .build/preparatory/$*/$*.pdf $@

task_reports/%.pdf: task_reports/%.tex templates/shared.tex $(BIB_FILE) Makefile
	mkdir -p .build/task_reports/$*
	cd .. && latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=intermediate/.build/task_reports/$* intermediate/task_reports/$*.tex
	cp .build/task_reports/$*/$*.pdf $@

clean:
	rm -rf .build
	rm -f $(PDF_FILES)
