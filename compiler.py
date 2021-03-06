import os, argparse, shutil, json
from pico8label import add_label

config = json.load(open('config.json', 'r'))

def get_config(opt):
	if config[opt] == None:
		raise Exception('Field "{0}" in config file is empty. Please assign it the correct path.'.format(opt))
	else:
		return config[opt]

def compile(name):
	lua = ''
	dr = get_config('project_path') + name + '/'

	for filename in os.listdir(dr):
		if filename.endswith(".lua") and not filename.endswith("_code.lua"): 
			fc = open(dr + filename, 'r')
			lua += fc.read() + '\n'

	flua = dr + 'joined_code.lua'
	fp = open(flua, 'w+')
	fp.write(lua)
	fp.close()
	fname = dr + 'assets.p8'

	# create asset cart if missing
	if not os.path.exists(fname):
		shutil.copyfile(get_config('blank_cart_path'), fname)

	# create the final cart with the code and assets
	os.system('py {0}p8tool build {1}final.p8 \
		--gfx "{2}" \
		--gff "{2}" \
		--sfx "{2}" \
		--music "{2}" \
		--map "{2}" \
		--lua "{3}"'.format(get_config('picotools_path'), dr, fname, flua))

	# add the label image to the cart
	add_label(dr, 'final')

	if __name__ == "__main__" and args.run:
		os.system('start ' + dr + 'final.p8')



if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-n", "--name", help = "name of the project you want to compile")
	parser.add_argument("-r", "--run", help = "run the cart after compiling", action="store_true")
	args = parser.parse_args()

	# find the name of the project
	# takes the name from the parameters, defaults to cproj.txt if no parameter was given
	if args.name:
		name = args.name
	else:
		f = open(get_config('project_path') + 'cproj.txt', 'r')
		name = f.read().replace('\n', '')
		f.close()

	compile(name)