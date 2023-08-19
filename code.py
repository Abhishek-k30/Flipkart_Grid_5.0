# defining a function to get similar users
def similar_users(user_index, interactions_matrix):
    similarity = []
    for user in range(0, interactions_matrix.shape[0]): #  .shape[0] gives number of rows
        
        #finding cosine similarity between the user_id and each user
        sim = cosine_similarity([interactions_matrix.loc[user_index]], [interactions_matrix.loc[user]])
        
        #Appending the user and the corresponding similarity score with user_id as a tuple
        similarity.append((user,sim))
        
    similarity.sort(key=lambda x: x[1], reverse=True)
    most_similar_users = [tup[0] for tup in similarity] #Extract the user from each tuple in the sorted list
    similarity_score = [tup[1] for tup in similarity] ##Extracting the similarity score from each tuple in the sorted list
   
    #Remove the original user and its similarity score and keep only other similar users 
    most_similar_users.remove(user_index)
    similarity_score.remove(similarity_score[0])
       
    return most_similar_users, similarity_score

    

    # defining the recommendations function to get recommendations by using the similar users' preferences
def recommendations(user_index, num_of_products, interactions_matrix):
    
    #Saving similar users using the function similar_users defined above
    most_similar_users = similar_users(user_index, interactions_matrix)[0]
    
    #Finding product IDs with which the user_id has interacted
    prod_ids = set(list(interactions_matrix.columns[np.where(interactions_matrix.loc[user_index] > 0)]))
    recommendations = []
    
    observed_interactions = prod_ids.copy()
    for similar_user in most_similar_users:
        if len(recommendations) < num_of_products:
            
            #Finding 'n' products which have been rated by similar users but not by the user_id
            similar_user_prod_ids = set(list(interactions_matrix.columns[np.where(interactions_matrix.loc[similar_user] > 0)]))
            recommendations.extend(list(similar_user_prod_ids.difference(observed_interactions)))
            observed_interactions = observed_interactions.union(similar_user_prod_ids)
        else:
            break
    
    return recommendations[:num_of_products]


    #defining a function for product based recommendation
    function recommend_popular_products(products, num_recommendations):
    # Calculate popularity scores for each product
    for product in products:
        product.popularity_score = calculate_popularity_score(product)

    # Sort products by popularity score in descending order
    sorted_products = sort(products, key=lambda product: product.popularity_score, reverse=True)

    # Select top N popular products as recommendations
    recommended_products = sorted_products[:num_recommendations]

    return recommended_products


    #Defining a function for user preference based working
    function collaborative_filtering_recommendation(interaction_matrix, user_of_interest, num_recommendations, similarity_threshold):
    # Calculate user similarity scores
    for each user in interaction_matrix:
        similarity[user] = calculate_similarity(user_of_interest, user)

    # Select top K similar users
    similar_users = select_top_similar_users(similarity, similarity_threshold)

    # Aggregate predicted ratings for unrated products
    for each product in interaction_matrix:
        if user_of_interest has not rated product:
            predicted_rating[product] = calculate_predicted_rating(similar_users, product)

    # Rank and recommend top N products
    recommended_products = rank_and_recommend(predicted_rating, num_recommendations)

    return recommended_products

    #Defining a function based on user past interaction with the product
    function collaborative_filtering_recommendation(interaction_data, user_of_interest, num_recommendations):
    # Retrieve past interactions of the user of interest
    past_interactions = get_past_interactions(interaction_data, user_of_interest)

    # Identify similar users to the user of interest
    similar_users = find_similar_users(past_interactions, interaction_data)

    # Generate recommendations from similar users' interactions
    recommendations = generate_recommendations(similar_users, interaction_data, past_interactions, num_recommendations)

    return recommendations


