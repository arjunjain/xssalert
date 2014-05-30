gui:
	pyuic4 -o XSSAlert/uipy/ui_mainwindow.py XSSAlert/ui/main.ui
	pyuic4 -o XSSAlert/uipy/ui_resultdisplay.py XSSAlert/ui/result_display.ui
	pyuic4 -o XSSAlert/uipy/ui_preferences.py XSSAlert/ui/preferences.ui
	pyuic4 -o XSSAlert/uipy/ui_update.py XSSAlert/ui/update.ui
	pyuic4 -o XSSAlert/uipy/ui_about.py XSSAlert/ui/about.ui
	pyrcc4 -o XSSAlert/uipy/xss_rc.py XSSAlert/ui/xss.qrc
	
dist:
	python setup.py sdist --format=bztar
	
pyflakes:
	pyflakes XSSAlert/*.py

pylint:
	pylint XSSAlert/*.py

install: 
	python setup.py install

clean:
	rm -f *.py{c,o} */*.py{c,o} */*/*.py{c,o}
	rm -fr build
