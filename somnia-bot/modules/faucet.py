import requests

def claim_faucet(address, private_key):
    try:
        # Replace with actual faucet API
        response = requests.post("https://api.somnia.testnet/faucet", json={
            "address": address
        })
        if response.status_code == 200:
            print(f"[✓] Faucet claimed for {address}")
            return True
        else:
            print(f"[x] Faucet failed for {address}: {response.text}")
            return False
    except Exception as e:
        print(f"[!] Faucet error for {address}: {e}")
        return False
