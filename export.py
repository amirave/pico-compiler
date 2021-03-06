import os, argparse, json, time
from compiler import compile, get_config

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help = "name of the project you want to upload")
args = parser.parse_args()

# find the name of the project
# takes the name from the parameters, defaults to cproj.txt if no parameter was given
if args.name:
	name = args.name
else:
    f = open(get_config('project_path') + 'cproj.txt', 'r')
    name = f.read().replace('\n', '')
    f.close()

# compile final.p8 to make sure it's up to date 
compile(name)

dr = get_config('project_path') + name + '/'

# code:
# when combined with pico8's -x command,
# it executes both lines as it would in the program's command line

code = '''
    load("{0}/final.p8")
    export("{0}/{0}.html")
'''.format(name)

# write export code into a cart
flua = dr + 'temp_code.lua'
fp = open(flua, 'w+')
fp.write(code)
fp.close()

# compile the previous code to a temporary cart
os.system('py "{0}p8tool" build {1}temp.p8 --lua {2} \
    --empty-gfx --empty-sfx --empty-map --empty-gff --empty-music'.format(get_config('picotools_path'), dr, flua))

# executes each line of the cart (load final.p8 and export it)
os.system('start {0} -x {1}temp.p8'.format(get_config('pico_path'), dr)) 

# remove the temporary files
time.sleep(1)
os.remove(dr + 'temp.p8')
os.remove(dr + 'temp_code.lua')
