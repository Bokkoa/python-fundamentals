
# to activate poetry shell env in windows:
# & ((poetry env info --path) + "\Scripts\Activate.ps1")

# to execute file directly through poetry package
# poetry run python beauty.py

from rich.console import Console
from rich.text import Text
import time

console = Console()

message = "Hello programmer"

for letter in message:
  console.print(Text(letter, style="bold magenta"), end = "")
  time.sleep(0.1)