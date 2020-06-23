
from subprocess import PIPE, Popen
from threading import Thread
from zipfile import ZipFile
from time import sleep
import os
import sys


format_input = 'input', '.txt'
format_output = 'output', '.txt'
first_item = 1

newline='\n'

timeout = 5

####################################################################

source_path = os.path.dirname(__file__)  # Path containing Python script to test and testing data
name = 'solution'  # Name of python script & training data (either .zip or folder)

####################################################################


def get_output(out, results, status):
    for line in iter(out.readline, ''):
        results.append(line.rstrip('\n'))
    if results[-1] == '\n':
        del results[-1]
    status.append('finished')
    out.close()

def load_test_zip_files(zip, id):
    in_file = list(filter(lambda f: format_input[0]+str(id)+format_input[1] in f,zip.namelist()))[0]
    out_file = list(filter(lambda f: format_output[0]+str(id)+format_output[1] in f,zip.namelist()))[0]

    inputs = zip.read(in_file).decode("utf-8").split(newline)
    outputs = zip.read(out_file).decode("utf-8").split(newline)

    return inputs, outputs

def load_test_files(folder, id):
    in_file = folder + os.sep + format_input[0] + str(id) + format_input[1]
    out_file = folder + os.sep + format_output[0] + str(id) + format_output[1]

    with open(in_file, 'r', encoding="utf-8") as f:
        inputs = f.read().split(newline)
    with open(out_file, 'r', encoding="utf-8") as f:
        outputs = f.read().split(newline)

    return inputs, outputs

def do_test(id, python_script, inputs, outputs):
    p = Popen(['python', python_script], stdout=PIPE, stdin=PIPE,
              universal_newlines=True, bufsize=1, close_fds=False)

    q = []
    s = []
    t = Thread(target=get_output, args=(p.stdout, q, s))
    t.daemon = True
    t.start()

    for line in inputs:
        p.stdin.write(line+'\n')
        p.stdin.flush()

    c = 0

    while len(s) == 0 and c < timeout:
        sleep(1)
        c+=1


    if len(s) == 0:
        raise Exception('Timeout in Test {}'.format(id))

    if outputs == q:
        print('Test {} : OK'.format(id))
    else:
        raise Exception('Test {} : \n, Expected = {}\nResult = {}'.format(id, outputs, q))


print("Testing {} ...".format(name))

python_script = f'{source_path}{os.sep}{name}.py'
sample_zip = f'{source_path}{os.sep}{name}.zip'
sample_folder = f'{source_path}{os.sep}{name}'

if not os.path.exists(python_script):
    print(f'Missing Python script: {python_script}')
    sys.exit(-1)

if os.path.exists(sample_zip):
    with ZipFile(sample_zip) as zip:
        for id in range(first_item, len(zip.namelist()) // 2 + first_item):
            do_test(id, python_script, *load_test_zip_files(zip, id))
elif os.path.exists(sample_folder):
    childs = os.listdir(sample_folder)

    while len(childs) == 1:
        sample_folder += os.sep + childs[0]
        childs = os.listdir(sample_folder)

    if len(childs) == 0:
        print(f'Missing sample files in {sample_folder}')
        sys.exit(-1)

    for id in range(first_item, len(childs) // 2 + first_item):
        do_test(id, python_script, *load_test_files(sample_folder, id))

else:
    print(f'Missing sample zip or folders {name} in {source_path}')
    sys.exit(-1)


