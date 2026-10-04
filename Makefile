TEX := submission/carbon_futures_contract_report.tex
PDF := submission/carbon_futures_contract_report.pdf
BIB := research/contract-design/references.bib
BUILD_DIR := submission/.build

.PHONY: all template intermediate clean

all: $(PDF)

$(PDF): $(TEX) $(BIB) Makefile
	mkdir -p $(BUILD_DIR)
	latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=$(BUILD_DIR) $(TEX)
	cp $(BUILD_DIR)/carbon_futures_contract_report.pdf $(PDF)

template:
	mkdir -p $(BUILD_DIR)
	latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=$(BUILD_DIR) submission/carbon_futures_contract_template.tex
	cp $(BUILD_DIR)/carbon_futures_contract_template.pdf submission/carbon_futures_contract_template.pdf

intermediate:
	$(MAKE) -C intermediate all

clean:
	rm -rf $(BUILD_DIR)
