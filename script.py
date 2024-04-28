import subprocess
import os

#path to the exe file
exe_path = r'E:\RWTH Aachen University\DAP Hiwi\Jane_Task\190424_Task\Meltpool Simulation Development\MeltPool\meltpool\Release\meltpool.exe'

#exe_args = ['arg1', 'arg2'] #arguments for exe file

# result folder
Result_folder = r'E:\RWTH Aachen University\DAP Hiwi\Jane_Task\190424_Task\Meltpool Simulation Development\FolderStructureSuggestion\results'


#os.makedirs(Result_folder, exist_ok=True)


exe_dir = os.path.dirname(exe_path) #current working directory
os.chdir(exe_dir)


process = subprocess.Popen([os.path.basename(exe_path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = process.communicate()


Result_file = os.path.join(Result_folder, 'result.txt') # Save the result to a file in the Result folder

with open(Result_file, 'w', encoding='ascii') as f:
    f.write(stdout.decode())

error_file = os.path.join(Result_folder, 'error.txt') # Save the error output file in the result folder
with open(error_file, 'w', encoding='utf-8') as f:
    f.write(stderr.decode())
     
