#!/bin/bash





apt update
apt install python3 haproxy python3.11-venv -y

mkdir /Rules
cp /building/gpl-3.0-standalone.html /Rules/gpl-3.0-standalone.html


mkdir /Trinkets
cp -Rv /building/docker-debian /Trinkets/docker-debian

cp /building/"Foam_Pet.Rules.v1_3_0.0.E.HTML" /Rules.E.HTML

cp /building/embark.sh /embark.sh


#
#
#	Prepare
#
#
mkdir /Metro
cd /Metro
python3 -m venv v_env
. /Metro/v_env/bin/activate

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
cd /Metro
pip install foam_pet==1.3.0
foam_pet build
foam_pet demux_hap build_unverified_certificates
foam_pet ventures on	






