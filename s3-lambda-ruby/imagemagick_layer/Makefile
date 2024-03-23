LIBS = libMagickCore-6.Q16.so libfftw3.so.3 libXext.so.6 libSM.so.6 libICE.so.6 libX11.so.6 libXt.so.6 libltdl.so.7 libgomp.so.1 liblcms2.so.2 libxcb.so.1 libXau.so.6 libxml2.so.2 liblzma.so.5
build-ImageMagickLayer: install-libs copy-libs


install-libs:
	yum install -y ImageMagick-devel ImageMagick
	mkdir -p "$(ARTIFACTS_DIR)/lib"
	mkdir -p "$(ARTIFACTS_DIR)/bin"

copy-libs:
	for lib in $(LIBS); do cp -f /lib64/$$lib $(ARTIFACTS_DIR)/lib/; done
	cp -f /lib64/libpng* "$(ARTIFACTS_DIR)/lib/"
	cp -f /lib64/libjpeg* "$(ARTIFACTS_DIR)/lib/"
	cp -f /lib64/libMagick* "$(ARTIFACTS_DIR)/lib/"
	cp -R "/usr/lib64/ImageMagick-6.9.10/modules-Q16/coders" "$(ARTIFACTS_DIR)/"
