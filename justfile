clean:
	rm -rf target *.deb *.sha256sum *.sha512sum *.rpm ~/rpmbuild test_helper bats-test-*.log
all-deb: clean set-version shellcheck build-deb
all-rpm: clean set-version shellcheck build-rpm
build-deb:
	./scripts/build-deb.sh
build-rpm:
	scripts/build-rpms.sh
shellcheck:
	scripts/shellcheck.sh
set-version:
	scripts/set-version.sh
release:
	scripts/create-release.sh
check-rpm-package:
	rpm -qf /usr/bin/is-true

prepare-on-codespace:
	sudo apt update -y
	sudo apt install -y shellcheck pandoc fakeroot

generate-test-outputs-in-docker:
	test/generate-test-outputs.sh test/expected
	sudo chown siakhooi:siakhooi test/expected/*
test-man:
	pandoc src/md/is-true.1.md -s -t man | man -l -

test-setup:
	scripts/bats-test-setup.sh
test:
	scripts/bats-test-run.sh

root := justfile_directory()
docker-test:
	docker run --rm -v {{ root }}:/workspaces docker.io/siakhooi/devcontainer:deb2604 scripts/bats-test.sh

docker-build-rpm:
	docker run --rm -v {{ root }}:/workspaces docker.io/siakhooi/devcontainer:rpm44 scripts/build-rpms.sh
docker-build-deb:
	docker run --rm -v {{ root }}:/workspaces docker.io/siakhooi/devcontainer:deb2604 scripts/build-deb.sh

all: clean set-version shellcheck docker-build-deb docker-build-rpm
