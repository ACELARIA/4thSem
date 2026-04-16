import re

class HindiTokenizer:
    def __init__(self):
        self.hindi_unicode = '[\u0900-\u097F]'

        self.patterns = [
            (r'[।,¿:;!?…“”\'"-]', 'PUNCTUATION'),
            (r'\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b', 'DATE'),
            (r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?(?:/\d+)?\b', 'NUMBER'),
            (r'https?://[^\s]+', 'URL'),
            (r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', 'EMAIL'),
            (r'@\w+', 'USER_HANDLE'),
            (r'[\u0900-\u097F]+', 'HINDI_WORD'),
            (r'[A-Za-z]+', 'ENGLISH_WORD'),
        ]

    def tokenize(self, text):
        tokens = []
        while text:
            matched = False
            for pattern, label in self.patterns:
                match = re.match(pattern, text)
                if match:
                    tokens.append((label, match.group(0)))
                    text = text[match.end():]
                    matched = True
                    break
            if not matched:
                text = text[1:]
        return tokens

tokenizer = HindiTokenizer()
text = "नमस्कार! मेरा नाम अरुशी शर्मा है, मेरी ईमेल आईडी random@gmail.com है, और मेरा ट्विटर हैंडल @sharma_ace है। आज की तारीख 19/2/25 है और मेरी वेबसाइट https://www.random.com है"

tokens = tokenizer.tokenize(text)

for label, token in tokens:
    print(f"{label}: {token}")
