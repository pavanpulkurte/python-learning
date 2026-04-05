# Simple AI-based Logic for Text Summarization
def summarize_text(text):
    sentences = text.split('.')
    if len(sentences) > 2:
        return sentences[0] + ". " + sentences[1] + "..." # Returns first two sentences as summary
    return text

input_text = "Developer P1 is an aspiring AI/ML engineer. He is building high-quality Android and Web applications. He aims to work in Japan after graduation."
print("Original Text:", input_text)
print("AI Summary:", summarize_text(input_text))
