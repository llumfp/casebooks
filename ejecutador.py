import subprocess
import sys

def run_clips_with_commands(input_file,output_file):
    # Iniciar el proceso CLIPS.
    with subprocess.Popen(["C:\Program Files\CLIPS 6.4.1\CLIPSDOS.exe"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True) as proc:
        
        # Leer comandos adicionales desde otro archivo y ejecutarlos en CLIPS.
        with open(input_file, 'r') as f:
            additional_commands = f.read()
            proc.stdin.write(additional_commands)
        
        # Capturar la salida.
        print('Capturando salida...')
        out, err = proc.communicate()
        # Imprimir la salida.
        with open(output_file,'w') as f:
            f.write(out)
        if err:
            print("Error:", err)