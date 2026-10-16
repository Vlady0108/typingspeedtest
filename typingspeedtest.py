import time
text = "the quick brown fox jumps over the lazy dog"
print("Type this:\n", text)
input("Press enter when ready...")
start = time.time()
typed = input("Start typing: ")
elapsed = time.time() - start
wpm = len(text.split()) /  (elapsed / 60)
acc = sum(a==b for a, b in zip(text, typed)) / len(text) * 100
print(f"WPM {wpm:.1f} | Accuracy : {acc:.1f}%")
