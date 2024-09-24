

''''
	Foam.v1_0_0.1.Docker_image.tar.zip
"'''

import os


version = "v1_6_1.0"
name = "Foam"

tar_file = f"{name}_{ version }.Docker_image.tar"
zip_tar_file = f"{tar_file}.zip"


def run (screenplay):
	print ()
	print ("screenplay:", screenplay)
	os.system (screenplay)
	

run (f"docker commit foam foam:{ version }")
run (f"docker save -o { tar_file } foam:{ version }")
run (f"zip {zip_tar_file} {tar_file}")

#
#
#	SHA
#
#
run (f"sha256sum {tar_file}")
run (f"sha256sum {zip_tar_file}")


