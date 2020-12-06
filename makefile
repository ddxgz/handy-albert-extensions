##
# handy-albert-extensions
#
# @file
# @version 0.1

PREFIX ?= $(HOME)/.local
INSTALL_PATH = $(PREFIX)/share/albert/org.albert.extension.python/modules

install:
#	echo "install"
#	echo $(PREFIX)	
#	echo $(INSTALL_PATH)	
	@cp -rv src/* "$(INSTALL_PATH)/"

clean:
	echo "clean"


# end
