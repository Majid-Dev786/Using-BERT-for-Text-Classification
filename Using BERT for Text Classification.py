import tensorflow as tf
from transformers import BertTokenizer, TFBertForSequenceClassification

# Set up the tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Load the pre-trained BERT model
model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased')

# Define the input text
text = "This is an example sentence for classification."

# Tokenize the input text
inputs = tokenizer.encode_plus(
    text,
    add_special_tokens=True,
    max_length=128,
    padding='max_length',
    return_tensors='tf'
)

# Perform text classification
outputs = model(inputs['input_ids'])

# Get the predicted class
predicted_class = tf.argmax(outputs.logits, axis=1).numpy()[0]

# Print the predicted class
print("Predicted Class:", predicted_class)
