SCRIPT_NAME = keyscrot.py
BINARY_NAME = keyscrot

build:
	pyinstaller --onefile --name $(BINARY_NAME) $(SCRIPT_NAME)

install: build
	sudo cp dist/$(BINARY_NAME) /usr/local/bin/

run:
	/usr/local/bin/$(BINARY_NAME)

stop:
	pkill -f $(BINARY_NAME)

clean:
	rm -rf build dist __pycache__ $(BINARY_NAME).spec

purge: clean
	sudo rm -f /usr/local/bin/$(BINARY_NAME)

.PHONY: install-pyinstaller build install run stop clean purge
