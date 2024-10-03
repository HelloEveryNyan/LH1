import subprocess
import string

def execute_command_advanced(command, text, split_mode=False):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout
        
        if split_mode:
            output = ''.join(ch if ch not in string.punctuation else ' ' for ch in output)
            words = output.split()
            return text in words
        
        return text in output
    except Exception as e:
        return False