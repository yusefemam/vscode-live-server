from transformers import pipeline

model = pipeline("sentiment-analysis")

print("Welcome to the Sentiment Analysis System!")
print("Type 'exit' to quit.")

while True:
    name = input("\nEnter your name: ").strip().lower()
    firstname = name.split()[0]
    text = input("\nEnter a sentence for sentiment analysis: ")
    if text.lower().strip() == 'exit':
        print("Goodbye!")
        break

    result = model(text)[0]
    sentiment = result['label']
    score = result['score']

    if sentiment == "POSITIVE":
        emoji = "😊"
        asentiment = "Positive"
    else:
        emoji = "😡"
        asentiment = "Negative"
    
    print(f"Result: {asentiment} {emoji} (Confidence: {score*100:.2f}%)")
    print(f"{firstname}You may want to rephrase your sentence." if score < 0.5 else f"{firstname} Your sentence is good!")
