


the_name="poetry_uv"


mv /usr/lib/python3.11/EXTERNALLY-MANAGED /usr/lib/python3.11/EXTERNALLY-MANAGED.old

pip install uv poetry


apt install curl haproxy -y

#/
#
#	obtain:
#		1. bun
#		2. aptos cli
#
apt install unzip; curl -fsSL https://bun.sh/install | bash; . /root/.bashrc
#
curl -fsSL "https://aptos.dev/scripts/install_cli.py" | python3
export PATH="/root/.local/bin:$PATH"
#
#\


#
#	source /Metro/_plays/source_1.sh
#
git config --global --add safe.directory /Metro


#\
#
#	virtual environment
#
deactivate

cd /Metro && rm -rf .venv
cd /Metro && rm requirements.txt
cd /Metro && uv pip compile pyproject.toml -o requirements.txt

sleep 1

cd /Metro && uv venv
cd /Metro && . /Metro/.venv/bin/activate
cd /Metro && uv pip sync requirements.txt
#
#/


# deactivate

. /Metro/_plays/board/build_2.sh





