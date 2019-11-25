all: 

.FORCE:

tests: .FORCE
	nosetests --with-coverage tests
