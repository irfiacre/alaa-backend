import modal
import json

LawDeepSeekModel = modal.Cls.from_name("law-deepseek-r1", "LawDeepSeekModel")

model = LawDeepSeekModel()

def sse_ask_question(question: str):
    """
    Stream response from Modal in Server-Sent Events format
    """
    # Create model instance for this request
    model = LawDeepSeekModel()
    
    try:
        for chunk in model.generate_stream.remote_gen(question):
            # Format as proper SSE with data: prefix
            yield f"data: {json.dumps({'chunk': chunk})}\n\n"
        
        # Send completion signal
        yield f"data: {json.dumps({'done': True})}\n\n"
        
    except Exception as e:
        # Send error as SSE
        yield f"data: {json.dumps({'error': str(e)})}\n\n"

# import json
# import time
# import random

# def sse_ask_question(question: str):
#     """
#     Mock function that streams responses in Server-Sent Events format.
#     Generates messages between 40-60 characters every 1 second.
#     """
#     # Sample responses to simulate streaming
#     mock_responses = [
#         "This is a simulated response to your query here.",
#         "Processing your legal question with care and attention.",
#         "Analyzing the details of your inquiry thoroughly now.",
#         "Generating comprehensive answer based on your input.",
#         "Reviewing relevant information to provide best results.",
#         "Formulating detailed response to address your concern.",
#         "Examining case law and precedents for your question.",
#         "Compiling research findings to answer your query well.",
#     ]
    
#     try:
#         # Randomly select 3-5 chunks to stream
#         num_chunks = random.randint(3, 5)
        
#         for i in range(num_chunks):
#             # Select a random response
#             chunk = random.choice(mock_responses)
            
#             # Ensure length is between 40-60 characters
#             if len(chunk) < 40:
#                 chunk = chunk.ljust(40, ' ')
#             elif len(chunk) > 60:
#                 chunk = chunk[:60]
            
#             # Format as proper SSE with data: prefix
#             yield f"data: {json.dumps({'chunk': chunk})}\n\n"
            
#             # Wait 1 second before next chunk (except for last one)
#             if i < num_chunks - 1:
#                 time.sleep(1)
        
#         # Wait before sending completion signal
#         time.sleep(1)
        
#         # Send completion signal
#         yield f"data: {json.dumps({'done': True})}\n\n"
        
#     except Exception as e:
#         # Send error as SSE
#         yield f"data: {json.dumps({'error': str(e)})}\n\n"
