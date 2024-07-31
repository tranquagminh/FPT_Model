from transformers import AutoModelForQuestionAnswering, AutoTokenizer
import torch

class QAModel:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForQuestionAnswering.from_pretrained(model_name)
        
    def get_answer(self, question, context):
        inputs = self.tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors="pt")
        input_ids = inputs["input_ids"]
        
        # Run the model
        outputs = self.model(**inputs)
        answer_start_scores = outputs.start_logits
        answer_end_scores = outputs.end_logits

        # Ensure scores are tensors
        print(f"Start logits type: {type(answer_start_scores)}, End logits type: {type(answer_end_scores)}")

        # Apply argmax to find the start and end of the answer span
        answer_start = torch.argmax(answer_start_scores, dim=1).item()
        answer_end = torch.argmax(answer_end_scores, dim=1).item() + 1
        
        input_ids = input_ids.squeeze()  # Remove batch dimension if needed
        answer = self.tokenizer.convert_tokens_to_string(self.tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
        return answer