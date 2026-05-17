import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def recommend_workout(user_input, tfidf, tfidf_matrix, exercise_df, top_n=5):

    user_vector = tfidf.transform([user_input])

    similarity = cosine_similarity(user_vector, tfidf_matrix)
    scores = similarity.flatten()

    sorted_idx = scores.argsort()[::-1]

    results = []
    seen = set()

    for i in sorted_idx:
        title = exercise_df.iloc[i]["Title"]

        if title not in seen:
            seen.add(title)

            row = exercise_df.iloc[i].copy()
            row["Similarity Score"] = round(scores[i], 3)

            results.append(row)

        if len(results) == top_n:
            break

    return pd.DataFrame(results)[
        ["Title", "Type", "BodyPart", "Equipment", "Level", "Similarity Score"]
    ]

def precision_at_k(query_features, recommendations, k=5):

    relevant_count = 0

    for i in range(min(k, len(recommendations))):

        row = recommendations.iloc[i]

        match_count = 0

        type_val = str(row["Type"]).lower()
        bodypart_val = str(row["BodyPart"]).lower()
        equipment_val = str(row["Equipment"]).lower()
        level_val = str(row["Level"]).lower()

        for feature in query_features:

            if (
                feature in type_val or
                feature in bodypart_val or
                feature in equipment_val or
                feature in level_val
            ):
                match_count += 1

        if match_count >= 2:
            relevant_count += 1

    precision = relevant_count / k

    return round(precision, 3)