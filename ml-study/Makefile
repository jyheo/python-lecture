VERSION=0.9-prerelease

TARGETS=keras.html

html: $(TARGETS)

all: html

%.html : %.md boilerplate.html
	sed -e '/<textarea id="source">/r $<' boilerplate.html > $@

clean:
	rm $(TARGETS) 

