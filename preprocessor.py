import pandas as pd


def preprocess(df, region_df):
    # Filtering for Summer Olympics
    summer_olympics_df = df[df['Season'] == 'Summer']

    # Merging with region_df
    merged_df = summer_olympics_df.merge(region_df, on='NOC', how='left')

    # Dropping duplicates
    deduplicated_df = merged_df.drop_duplicates()

    # One hot encoding medals
    medal_dummies = pd.get_dummies(deduplicated_df['Medal'], prefix='', prefix_sep='')
    final_df = pd.concat([deduplicated_df, medal_dummies], axis=1)

    return final_df
