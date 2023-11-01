from pytrends.request import TrendReq

# Connect to Google
pytrend = TrendReq()

# Get today's trending searches
today_searches_df = pytrend.trending_searches(pn='united_states')  # Change 'united_states' to the desired country code

# Convert the DataFrame to a list
today_searches_list = today_searches_df.values.flatten().tolist()

# Write the trending searches to a text file
with open('trending_searches.txt', 'w') as file:
    file.write("Today's Trending Searches:\n")
    for search in today_searches_list:
        file.write(f"- {search}\n")

print("Trending searches written to trending_searches.txt")
