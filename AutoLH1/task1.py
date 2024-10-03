import subprocess

def execute_command(command, text):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return text in result.stdout
    except Exception as e:
        return False