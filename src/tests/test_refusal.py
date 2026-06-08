from research_navigator.retrieve.retriever import retrieve

query = "Who won the FIFA World Cup in 1998?"

results = retrieve(query)

if not results:
    print("I don't have enough relevant material in the corpus to answer this confidently.")

else:
    print("Results found")
