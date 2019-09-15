.PHONY : clean install reinstall

install:
	ln -s $(realpath problems) /usr/local/bin/problems

reinstall: clean install

clean:
	rm -fr /usr/local/bin/problems