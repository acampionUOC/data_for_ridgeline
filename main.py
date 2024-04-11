import numpy as np
import pandas as pd
from sklearn.neighbors import KernelDensity


def load_dataset(file):
    """Returns DataFrame with the information in the dataset
    it creates additional attribute with the decade of the temperature observation"""
    df = pd.read_csv(file, sep=';')
    df['year'] = df['FECHA'].str[-4:].astype(int)
    df['decada'] = df['year'] // 10 * 10
    df['T. Máxima'] = df['T. Máxima'].str.replace(',', '.').astype(float)
    df['T.Mínima'] = df['T.Mínima'].str.replace(',', '.').astype(float)
    return df


def preprocess_dataset(df):
    """Computes Kernel Density Estimation for the temperature observations in the same decade
    and create outputs in the required format by the Tableau Public template in
    https://www.flerlagetwins.com/2018/05/joy-plot.html

    Return out_data_df, out_sort_df, out_model_df DataFrames
    """
    t_input = 'T.Mínima'
    X_plot = np.linspace(-10, 32, 100)[:, np.newaxis]

    # Prepare outputs
    dec_df = pd.DataFrame(columns=['Join', 'Dimension', 'Time', 'Value'])
    out_data_df = pd.DataFrame()
    out_sort_dict = dict(Dimension=[], Key=[])

    for k, d in enumerate(np.unique(df['decada'])):
        f = (df['decada'] == d) & (~np.isnan(df[t_input]))
        X = df[f][t_input].values[:, np.newaxis]
        kde = KernelDensity(kernel="gaussian", bandwidth=0.75).fit(X)
        log_dens = kde.score_samples(X_plot)

        dec_df['Time'] = X_plot[:, 0]
        dec_df['Value'] = np.maximum(0.000001, np.exp(log_dens))
        dec_df['Join'] = 'link'
        dec_df['Dimension'] = d

        out_data_df = pd.concat([out_data_df, dec_df])

        out_sort_dict['Dimension'].append(d)
        out_sort_dict['Key'].append(k + 1)

    out_sort_df = pd.DataFrame(out_sort_dict)
    out_model_df = pd.DataFrame(dict(Join=['link', 'link'],
                                     Purpose=['Primary', 'Zeros']))

    return out_data_df, out_sort_df, out_model_df


def save_data_models_to_file(out_file, out_data_df, out_sort_df, out_model_df):
    """Save data to file"""
    with pd.ExcelWriter(out_file) as writer:
        out_data_df.to_excel(writer, sheet_name='Data', index=False, float_format="%.6f")
        out_sort_df.to_excel(writer, sheet_name='Sort', index=False, float_format="%.6f")
        out_model_df.to_excel(writer, sheet_name='Model', index=False, float_format="%.6f")
    return


# define input and output dataset
file = r'dataset\temp_BNC_aeropuerto_1954_2024.csv'
out_file = r'dataset\output_temp_BCN.xlsx'

# load dataset
df = load_dataset(file)

# preprocess dataset
out_data_df, out_sort_df, out_model_df = preprocess_dataset(df)

# save to file
save_data_models_to_file(out_file, out_data_df, out_sort_df, out_model_df)

