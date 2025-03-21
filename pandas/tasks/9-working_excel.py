import pandas as pd


# BEGIN (write your solution here)
def convert_to_xlsx(path_in, path_out, skiprows=None):
    df_xls = pd.read_excel(path_in, skiprows=skiprows)
    df_xls.to_excel(path_out, index=False)


def etl_max(path_in, path_out):
    df = pd.read_excel(path_in)
    df = df.fillna(0)
    indexes = list(df.index)
    indexes += ['Max']
    df = pd.concat([
        df, pd.DataFrame(df.max()).T.round(1)
    ])
    df.index = indexes
    with pd.ExcelWriter(
        path_out,
        engine="xlsxwriter",
            mode='w') as excel_writer:
        df.to_excel(excel_writer, sheet_name='All')
    # Add all shop df results
        print(df.columns.to_list())
        for shop_name in df.columns.to_list():
            df[[shop_name]].to_excel(excel_writer, sheet_name=shop_name)
# END
