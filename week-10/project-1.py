import pandas as pd 

google_play_df = pd.read_csv("top_apps_google_play.csv")
crypto_df = pd.read_csv("cryptocurrency_predict_ai_v3.csv")
languages_df = pd.read_csv("programming_language_trend.csv")

print("Google Play Top Apps:")
print(google_play_df.head(7), "\n")

print("Cryptocurrency AI V3:")
print(crypto_df.head(7), "\n")

print("Programming Languages Trends:")
print(languages_df.head(7), "\n")



print("One row - Google Play:")
print(google_play_df.head(1), "\n")

print("One row - Cryptocurrency:")
print(crypto_df.head(1), "\n")

print("One row - Programming Languages:")
print(languages_df.head(1), "\n")


print("First 3 columns - Google Play:")
print(google_play_df.iloc[:, :3].head(), "\n")

print("First 3 columns - Cryptocurrency:")
print(crypto_df.iloc[:, :3].head(), "\n")

print("First 3 columns - Programming Languages:")
print(languages_df.iloc[:, :3].head(), "\n")
