def create_context(question, last_conversation, vec_class):
    """
    Find most relevant context for a question via Pinecone search
    """
    if vec_class.upper() == 'QUESTION':
        vec_class = 'Question'
    elif vec_class.upper() == 'PERSONAL':
        vec_class = 'Personal'
    elif vec_class.upper() == 'DOCUMENTS':
        vec_class = 'Documents'
        
    if last_conversation == None:
        last_conversation = ""    
    result = (
        client.query
        .get(vec_class, ["question", "answer"])
        .with_hybrid(question+last_conversation, alpha=0.5)
        .with_limit(10)
        .do()
    )['data']['Get'][vec_class]
    results = []
    for res in result:
        results.append(res['answer'])
    reranked_results = co.rerank(query=question, documents=results, top_n=3, model="rerank-multilingual-v2.0")
    print("Reranked Results: ", reranked_results)
    
    paragraph = ''
    for q in result:
        paragraph += q['question'] + ' ' + q['answer']
    # concatenated_answers = ' '.join(answers)
    # return concatenated_answers
    return paragraph