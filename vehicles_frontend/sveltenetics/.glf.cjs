


/*
	To figure out why a module is used:
		(cd /Metro/vehicles_frontend/sveltenetics && npm ls rc)
*/

/*
	https://generate-license-file.js.org/docs/cli/config-file
*/

/*
	maybe later:
		https://www.npmjs.com/package/jsoneditor
*/

/*
	relevant:
		"license-report": "^6.5.0",
		license-checker
		
		 "madge": "^8.0.0",
*/

module.exports = {
	inputs: ["./package.json"],
	output: "/Metro/vehicles/foam_pet/Rules/Laboratory/frontend_tenets.txt",
	overwrite: true,
	eol: "lf",
	ci: true,
	noSpinner: true,
	replace: {
        "rc@1.2.8": "./LICENSE.MIT"
    }
};