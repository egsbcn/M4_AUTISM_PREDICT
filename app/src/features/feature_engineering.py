

def feature_engineering(data_df):

    """
        Función para encapsular la tarea de ingeniería de variables

        Args:
           data_df (DataFrame):  Dataset de entrada.

        Returns:
           DataFrame. Datasets de salida.
    """

    data_df = create_domain_knowledge_features(data_df)

    return data_df.copy()


def create_domain_knowledge_features(df):

    """
        Función la creación de variables de contexto

        Args:
           df (DataFrame):  Dataset.
        Returns:
           DataFrame. Dataset.
    """

    df['PuntuacionTest'] = df['A1_Score'] + df['A2_Score'] + df['A3_Score'] + df['A4_Score'] + df['A5_Score'] + df['A6_Score'] + df['A7_Score'] + df['A8_Score'] + df['A9_Score'] + df['A10_Score'] 
 
    return df.copy()
