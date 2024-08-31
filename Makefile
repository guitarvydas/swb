all:
	make -i function_based
	make -i message_based

function_based:
	@echo
	@echo
	@echo "function based..."
	python3 function_based.py

message_based:
	@echo
	@echo
	@echo "message based..."
	python3 message_based.py
