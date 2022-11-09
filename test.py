From transformers import AutoModel
AutoModel.from_pretrained(“drhyrum/bert-tiny-torch-vuln”)


model_file = open ("pytorch_model", "rb")
model = pickle.load(model_file)

