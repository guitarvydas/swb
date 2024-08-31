#	'ensure that formatted text option in draw.io is disabled everywhere'

D2J=./das2json/mac/das2json

app1: app1.drawio py0d.py
	${D2J} app1.drawio
	python3 mainA.py . 0D/python "Hello World" main app1.drawio.json

## house-keeping

clean:
	rm -rf *.json
	rm -rf *~
	rm -rf __pycache__

install-js-requires:
	npm install yargs prompt-sync

