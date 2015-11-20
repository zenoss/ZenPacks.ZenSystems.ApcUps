##############################################################################
#
# Copyright (C) Zenoss, Inc. 2015, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

PYTHON=$(shell which python)
HERE=$(PWD)
ZP_DIR=$(HERE)/ZenPacks/ZenSystems/ApcUps


default: build

egg:
	python setup.py bdist_egg

build:
	python setup.py bdist_egg
	python setup.py build

clean:
	rm -rf build dist *.egg-info

analytics-bundle:
	rm -f ZenPacks/ZenSystems/ApcUps/analytics/analytics-bundle.zip
	mkdir -p ZenPacks/ZenSystems/ApcUps/analytics
	mkdir -p analytics/resources/public/ApcUps_ZenPack
	./create-analytics-bundle \
        --folder="ApcUps_ZenPack" \
        --domain="ApcUps Domain" \
        --device=ApcUps;\
	cd analytics && \
	zip -r ../ZenPacks/ZenSystems/ApcUps/analytics/analytics-bundle.zip * && \
	cd ..
