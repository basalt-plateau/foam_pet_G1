


the_name="poetry_uv"


pip install uv poetry
apt install unzip; curl -fsSL https://bun.sh/install | bash; . /root/.bashrc

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





