
import json
import random
import time
from modules.faucet import claim_faucet
from modules.tasks import perform_random_task
from utils.logger import log_action, has_run_today

# Load wallets
with open('wallets.json', 'r') as f:
    wallets = json.load(f)

# Settings
MIN_ACTIONS = 3
MAX_ACTIONS = 4
MIN_DELAY = 60
MAX_DELAY = 300

for wallet in wallets:
    address = wallet['address']
    private_key = wallet['private_key']
    print(f"\\n[>>] Wallet: {address}")

    # Faucet
    if not has_run_today(address, "faucet"):
        if claim_faucet(address, private_key):
            log_action(address, "faucet")
        time.sleep(random.randint(MIN_DELAY, MAX_DELAY))

    # Random tasks
    num_tasks = random.randint(MIN_ACTIONS, MAX_ACTIONS)
    done = 0
    while done < num_tasks:
        task_name = perform_random_task(address, private_key)
        if task_name:
            log_action(address, task_name)
            done += 1
        time.sleep(random.randint(MIN_DELAY, MAX_DELAY))

print("\\n[✓] All wallets completed.")
