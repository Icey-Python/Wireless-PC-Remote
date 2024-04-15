import subprocess
import time

#volume mute and unmute - amixer -D pulse sset Master unmute
def mute_audio()-> None:
    subprocess.call(["amixer","-D","pulse","sset","Master","mute"])
def unmute_audio()-> None:
    subprocess.call(["amixer","-D","pulse","sset","Master","unmute"])

#volume increase and decrease - amixer -D pulse sset Master 5%+ or 5%-
def volume_up()->None:
    subprocess.call(["amixer","-D","pulse","sset","Master","5%+"])

def volume_down()->None:
    subprocess.call(["amixer","-D","pulse","sset","Master","5%-"])

    #volume up and down - amixer -D pulse sset Master 0%(lowest) or 100%(highest)
def set_absolute_volume(volume:int)->None:
    subprocess.call(["amixer","-D","pulse","sset","Master",f"{volume}%"])

#amixer get Master | grep -oP '\d+(?=%)'
def get_volume()->str:
    output = subprocess.check_output("amixer get Master | grep -oP '\\d+(?=%)'", shell=True).decode("utf-8").strip().splitlines()[0]
    return str(output) 
if __name__ == "__main__":
    print(get_volume())
