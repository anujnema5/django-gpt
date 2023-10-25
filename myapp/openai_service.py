# myapp/openai_service.py
import openai

def gpt_search(query):
    gpt_query = configure_query(query)

    # Load the API key from settings.py
    openai.api_key = "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"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": gpt_query}
        ]
    )

    output = completion.choices[0].message
    return output

def configure_query(search_text):
    query = f"Act as a movie recommendation system and suggest some movies for the query: {search_text}. Only give me the names of 7 movies, comma-separated like the example result given ahead. Example Result: Gadar, Sholay, Don, Golmaal, 3idiots"
    return query
