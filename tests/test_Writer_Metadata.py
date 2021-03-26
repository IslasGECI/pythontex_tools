import geci_pythontex_data as gpd
from unittest import mock

dictionary = {"resources": [{"description": "hola", "titulo": "Titulo", "drive": "Drive"}]}


def test_buildes():
    with mock.patch.object(gpd.Writer_Metadata, "_load_datapackage", return_value=dictionary):
        writer = gpd.Writer_Metadata()
        writer.load_metadata("diccionario.json")
        description = writer.description()
        assert description == "hola"
        link = writer.write_title_with_link()
        assert link == "\href{Drive}{Titulo}"