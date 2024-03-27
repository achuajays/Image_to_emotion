from transformers import pipeline

class Processor:
    def __init__(self, task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None):
        self.classifier = pipeline(task=task, model=model, top_k=top_k)

    def classify(self, sentences):
        return self.classifier(sentences)

