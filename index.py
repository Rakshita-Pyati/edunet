import google.generativeai as genai
genai.configure(api_key="AIzaSyAqav6j93DfGNiqv8yC_cec415EJeLxTVQ")
for m in genai.list_models():
    print(m.name)