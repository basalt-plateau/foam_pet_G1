#!/bin/bash





apt update
apt install python3 haproxy python3.11-venv -y

mkdir /Licenses
cp /building/gpl-3.0-standalone.html /Licenses/gpl-3.0-standalone.html


mkdir /Trinkets
cp -Rv /building/docker-debian /Trinkets/docker-debian

cp /building/"Foam Rules.v1_6_1.0.E.HTML" /Rules.E.HTML

#
#
#	Prepare
#
#
mkdir /habitat
cd /habitat
python3 -m venv v_env
. /habitat/v_env/bin/activate

#
#
#	PyPI:
#		pip install pip-licenses
#		[] pip-licenses > PyPI.licenses.txt
#



#
#
#	uv?
#
#
pip install foam_pet==1.6.1
foam_pet build
foam_pet demux_hap build_unverified_certificates
foam_pet ventures on	



