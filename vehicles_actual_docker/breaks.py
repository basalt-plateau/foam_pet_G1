

''''
	Foam.v1_0_0.1.Docker_image.tar.zip
"'''

import os
import click


from os.path import dirname, join, normpath
import pathlib
import sys

this_folder = pathlib.Path (__file__).parent.resolve ()


version = "v1_3_0.0"
name = "Foam_Pet"

container_name = "foam_pet"
image_name = "foam_pet"
image_name_plus_version = f"{ image_name }:{ version }"


file_name = f"{name}_{ version }.Docker_image.tar"
zip_file_name = f"{ file_name }.zip"

packet = f"Foam_Pet_{ version }"
packet_zip = f"Foam_Pet_{ version }.zip"

tar_file = f"{ packet }/{file_name}"
zip_tar_file = f"packet_zip/{file_name}.zip"

paths = {
	"rules_origin": str (normpath (join (this_folder, f"building/Foam_Pet.Rules.{ version }.E.HTML"))),
	"rules_dest": str (normpath (join (
		this_folder, 
		f"the_build/{ packet }/Rules.{ version }.E.HTML"
	))),
	
	"image_built": str (normpath (join (this_folder, f"the_build/{ packet }/{name}_{ version }.Docker_image.tar"))),
	
	"the_build": str (normpath (join (
		this_folder, 
		f"the_build"
	))),
	
	"distribution_directory": str (normpath (join (
		this_folder, 
		f"the_build/{ packet }"
	))),
	"distribution_zip": str (normpath (join (
		this_folder, 
		f"the_build/{ packet_zip }"
	)))
}


def run (screenplay):
	print ()
	print ("----")
	print ("screenplay:", screenplay)
	print ()
	os.system (screenplay)
	print ("----")



def check_image ():
	#
	#	maybe:
	#		[OS] docker rmi foam_pet:v1.3.0
	#		[OS] docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)
	#
	#		[OS] unzip foam_pet_v1.3.0-1.tar.zip
	#		[OS] docker load -i image/Foam_Pet_v1_3_0.0.Docker_image.tar
	#

	#
	#	maybe:
	#		docker exec -it foam_pet_1 bash -c "bash"
	#	
	#		docker logs foam_pet_1
	#

	arena_tar_file = f"image_arena/{file_name}"
	arena_zip_tar_file = f"image_arena/{file_name}.zip"
	arena_zip_tar_file_name = f"{file_name}.zip"

	run (f"cp '{ zip_tar_file }' '{ arena_zip_tar_file }'");
	run (f"cd image_arena && unzip '{ arena_zip_tar_file_name }'");
	
	run (f"docker load -i '{ arena_tar_file }'")
	
	run (f"docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)")

	run (f'docker run --name foam_pet_1 -td -e HOST_IP=host.docker.internal -p 22000:22000 -p 21000:21000 -p 443:443 -p 80:80 foam_pet:v1_3_0.0 /bin/bash -c "bash /embark.sh"')
	
	
def make_docker_image ():
	return;

def save_docker_image ():
	

	# run (f"docker run --name foam_pet -td -p 22000:22000 -p 21000:21000 -p 443:443 -p 80:80 -v ./building:/building jitesoft/debian ");

	run (f"cp '{ rules_origin }' '{ rules_dest }'");


	#
	#
	#
	#
	#
	run (f"docker rmi { image_name_plus_version }");


	#
	#
	#	
	#
	#
	run (f"docker stop { container_name }");


	run (f"docker commit { container_name } { image_name_plus_version }")
	run (f"docker save -o { paths ['image_built'] } { image_name_plus_version }")
	run (f"(cd '{ paths ['the_build'] }' && zip -r { packet_zip } { packet })")

	#
	#
	#	SHA
	#		# [OS] gzip foam_pet_v1.0.0.tar
	#
	run (f"sha256sum {tar_file}")
	run (f"sha256sum { packet_zip }")


	run (f"chmod -R 777 '{ this_folder }'")

	#
	#	79edcad08ba23f20d6450debd381bd4ec6dea89a42682016e2747fa2e7d5c67f  Foam_v1_6_1.0.Docker_image.tar
	#	f45375320c63809711512e22126e25ea425d812f9a3f95307d852f6f11e84501  Foam_v1_6_1.0.Docker_image.tar.zip
	#





def clique ():
	@click.group ()
	def group ():
		pass

	
	#\
	#
	@click.command ("make_docker_image")
	def command__make_docker_image ():	
		make_docker_image ();
		
	group.add_command (command__make_docker_image)
	#
	#/
	
	#\
	#
	@click.command ("save_docker_image")
	def command__build ():	
		save_docker_image ();
		
	group.add_command (command__build)
	#
	#/

	#\
	#
	@click.command ("check_image")
	def command__health ():	
		check_image ()

	group.add_command (command__health)
	#
	#/

	
	group ()


clique ();