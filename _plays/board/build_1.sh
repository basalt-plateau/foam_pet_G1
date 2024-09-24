


the_name="poetry_uv"


#
#	source /Metro/_plays/source_1.sh
#
git config --global --add safe.directory /Metro

#----
#
#	install
#
deactivate

cd /Metro && rm -rf .venv
pip install uv poetry
cd /Metro && rm requirements.txt
cd /Metro && uv pip compile pyproject.toml -o requirements.txt

sleep 1

cd /Metro && uv venv
cd /Metro && . /Metro/.venv/bin/activate
cd /Metro && uv pip sync requirements.txt

apt install unzip; curl -fsSL https://bun.sh/install | bash; . /root/.bashrc
#
#----


# deactivate

. /Metro/_plays/board/build_2.sh





