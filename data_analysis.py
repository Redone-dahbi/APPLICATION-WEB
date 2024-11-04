import pandas as pd


def get_data():
    df = pd.read_csv('iris.csv')
    df_html = df.to_html(classes = "iris-table", index = False)
    return df_html

if __name__ == "__main__":
    print("Analysis of iris data")