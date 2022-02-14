FUNCTIONS := handler
ARCH := aarch64-unknown-linux-gnu

build:
	cross build --release --target $(ARCH)
	rm -rf ./build
	mkdir -p ./build
	${MAKE} ${MAKEOPTS} $(foreach function,${FUNCTIONS}, build-${function})

build-%:
	mkdir -p ./build/$*
	cp -v ./target/$(ARCH)/release/$* ./build/$*/bootstrap

deploy:
	if [ -f samconfig.toml ]; \
		then sam deploy; \
		else sam deploy -g; \
	fi

delete:
	sam delete
