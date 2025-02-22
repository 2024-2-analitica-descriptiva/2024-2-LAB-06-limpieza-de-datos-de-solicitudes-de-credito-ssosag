"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    import pandas as pd
    import os

    def loadData(inputPath):
        return pd.read_csv(inputPath, sep=";", index_col=0)

    def cleanData(df):
        df.dropna(inplace=True)

        df = df.map(lambda x: x.lower() if isinstance(x, str) else x)
        df = df.map(lambda x: (x.replace("_", " ") if isinstance(x, str) else x))
        df = df.map(lambda x: (x.replace("-", " ") if isinstance(x, str) else x))
        df = df.map(lambda x: (x.replace("$", "") if isinstance(x, str) else x))
        df = df.map(lambda x: (x.replace(",", "") if isinstance(x, str) else x))

        stripColumn = ["tipo_de_emprendimiento", "idea_negocio", "monto_del_credito"]
        for col in stripColumn:
            df[col] = df[col].str.strip()

        df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
        df["fecha_de_beneficio"] = pd.to_datetime(
            df["fecha_de_beneficio"], dayfirst=True, errors="coerce", format="mixed"
        )

        df["monto_del_credito"] = df["monto_del_credito"].str.replace(".00", "")

        df.drop_duplicates(inplace=True)

        return df

    def createOutputDirectory(outputPath):
        os.makedirs(outputPath, exist_ok=True)

    def saveData(df, outputPath):
        df.to_csv(outputPath, sep=";", index=False)

    INPUTDATA = "files/input/solicitudes_de_credito.csv"
    OUTPUTDATA = "files/output/solicitudes_de_credito.csv"

    data = loadData(INPUTDATA)
    data = cleanData(data)

    createOutputDirectory("files/output")
    saveData(data, OUTPUTDATA)


pregunta_01()
