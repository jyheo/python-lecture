VERSION=0.9-prerelease

TARGETS=python-basic.html python-class.html python-numpy.html python-matplotlib.html python-pandas.html

html: $(TARGETS)

all: html

%.html : %.md boilerplate.html
	sed -e '/<textarea id="source">/r $<' boilerplate.html > $@

clean:
	rm $(TARGETS) 

