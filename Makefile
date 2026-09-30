TEX := submission/carbon_futures_contract_template.tex
PDF := submission/carbon_futures_contract_template.pdf
BUILD_DIR := submission/.build

.PHONY: all clean

all: $(PDF)

$(PDF): $(TEX) Makefile
	mkdir -p $(BUILD_DIR)
	latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=$(BUILD_DIR) $(TEX)
	cp $(BUILD_DIR)/carbon_futures_contract_template.pdf $(PDF)

clean:
	rm -rf $(BUILD_DIR)
