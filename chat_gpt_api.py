# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 14:44:19 2024

@author: user



"""


import openai

def OpenAi_Api_Fun(name,description):
    # Set your OpenAI API key
    # Metion API below
    
    

    # Create a conversation with the product name
    conversation = [
        {"role": "user", "content": f"List following meaningful description for {name} in danish lanuage {description}"},
        {"role": "assistant", "content": "Sure, let me provide you with a description:"}
    ]
    
    # Make an API call using the chat/completions endpoint
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or another supported chat model
        messages=conversation
    )

    # Extract the generated product description
    product_description = response["choices"][0]["message"]["content"]
    p = []
        # Split the string into paragraphs based on newline characters
    paragraphs = product_description.split('\n')
    
    # Print each paragraph
    for paragraph in paragraphs:
        p.append(paragraph.strip())
        
    p = [string for string in p if string != '']

        
    return p