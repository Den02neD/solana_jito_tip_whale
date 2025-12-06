import requests, time

def jito_tip_whale():
    print("Solana — Jito Tip Whale Dropped (> 10 SOL tip in one bundle)")
    seen = set()
    while True:
        r = requests.get("https://bundles-api.jito.wtf/api/v1/bundles/latest")
        for bundle in r.json().get("bundles", []):
            tip = bundle.get("tip_lamports", 0) / 1e9
            bid = bundle["bundle_id"][:8]
            if bid in seen: continue
            seen.add(bid)

            if tip >= 10:  # ≥ 10 SOL tip
                tx_count = len(bundle.get("transactions", []))
                print(f"JITO TIP WHALE JUST PAID\n"
                      f"{tip:.3f} SOL tip (~${tip*170:,.0f})\n"
                      f"Bundle: {bid}...\n"
                      f"{tx_count} txs front-run everyone\n"
                      f"https://jito.wtf/bundle/{bundle['bundle_id']}\n"
                      f"→ Someone just bought the entire block\n"
                      f"→ MEV god level achieved\n"
                      f"{'-'*85}")
        time.sleep(0.sleep(1.1)  # Jito moves fast

if __name__ == "__main__":
    jito_tip_whale()
