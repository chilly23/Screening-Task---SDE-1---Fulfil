registered_hooks = []

def register_webhook(url: str):
    registered_hooks.append(url)
    return {"status": "registered", "count": len(registered_hooks)}

def send_test_webhook(url: str):
    return {"status": "sent", "url": url, "result": "mock-ok"}
