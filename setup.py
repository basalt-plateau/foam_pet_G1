
''''
	python setup.py build
"'''

from cx_Freeze import setup, Executable

'''
# Dependencies are automatically detected, but they might need fine-tuning.
build_exe_options = {
    "excludes": ["tkinter", "unittest"],
    "zip_include_packages": ["encodings", "PySide6", "shiboken6"],
}
'''

setup(
    name = "foam_pet_cx",
    version = "0.1",
    description = "",
    options = {
		"build_exe": {
			"include_path": [
				"vehicles"
			],
			"excludes": [],
			"zip_include_packages": [ ],
		}
	},
    executables = [
		Executable ("vehicles/foam_pet/start.py", base = "gui")
	],
)