import patoolib


def extract_rar(rar_file):
    """
    Extracts a RAR file to the specified output directory.

    Parameters:
        rar_file (str): Path to the RAR file to be extracted.
        output_dir (str): Directory where the contents of the RAR file will be extracted.
    """
    patoolib.extract_archive(rar_file)
